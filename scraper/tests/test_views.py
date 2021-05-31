from django.test import TestCase
from scraper.models import Websites 
import json


class TestWebsiteConfigView(TestCase):

    @classmethod
    def setUpTestData(cls):
        Websites.objects.create(
            name='jobsdb',
            url='https://www.jobsdb.com'
        )

    def test_get_valid_config(self):
        expected_response = {
            'id': 1,
            'name': 'jobsdb',
            'url': 'https://www.jobsdb.com'
        }
        response = self.client.get('/scraper/config/?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_get_invalid_id(self):
        expected_response = {
            'message': 'id 2 do not exists'
        }
        response = self.client.get('/scraper/config/?id=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_get_invalid_id_param_type(self):
        expected_response = {
            'message': 'Invalid request'
        }
        response = self.client.get('/scraper/config/?id=random')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), expected_response)

    def test_create_config_pass(self):
        expected_response = {
            'id': 3,
            'name': 'linkedin',
            'url': 'https://www.linkedin.com/'
        }
        request_body = {
            'name': 'linkedin',
            'url': 'https://www.linkedin.com/'
        } 
        response = self.client.post(
            '/scraper/config/', data=json.dumps(request_body), content_type="application/json")
        self.assertEqual(response.json(), expected_response)

    def test_create_config_duplicate_name_fail(self):
        expected_response = {
            'message': 'Error creating config'
        }
        request_body = {
            'name': 'jobsdb',
            'url': 'https://www.jobsdb.com/'
        }
        response = self.client.post(
            '/scraper/config/', data=json.dumps(request_body), content_type="application/json")
        self.assertEqual(response.json(), expected_response)

    def test_create_config_empty_request(self):
        expected_response = {
            'message': 'Invalid request'
        }
        request_body = {}
        response = self.client.post(
            '/scraper/config/', data=json.dumps(request_body), content_type="application/json")
        self.assertEqual(response.json(), expected_response)

