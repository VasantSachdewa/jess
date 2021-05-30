from django.test import TestCase
from scraper.models import Websites 


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

