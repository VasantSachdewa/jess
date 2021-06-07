import unittest
from scraper.exceptions import InvalidScaperId
from unittest.mock import MagicMock, patch
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

    def test_create_config_empty_request_fail(self):
        expected_response = {
            'message': 'Invalid request'
        }
        request_body = {}
        response = self.client.post(
            '/scraper/config/', data=json.dumps(request_body), content_type="application/json")
        self.assertEqual(response.json(), expected_response)

    def test_patch_config_update_valid(self):
        expected_response = {
            'id': 1,
            'name': 'jobsdb',
            'url': 'https://www.jobsdbpatched.com'
        }
        request_body = {
            'id': 1,
            'url': 'https://www.jobsdbpatched.com'
        }
        response = self.client.put(
            '/scraper/config/', data=json.dumps(request_body), content_type="application/json")
        self.assertEqual(response.json(), expected_response)

    def test_patch_config_create_valid(self):
        expected_response = {
            'id': 4,
            'name': 'linkedin',
            'url': 'https://www.linkedin.com'
        }
        request_body = {
            'name': 'linkedin',
            'url': 'https://www.linkedin.com'
        }
        response = self.client.put(
            '/scraper/config/', data=json.dumps(request_body), content_type="application/json")
        self.assertEqual(response.json(), expected_response)

    def test_patch_invalid_id_fail(self):
        expected_response = {
            'message': 'Invalid request'
        }
        request_body = {
            'id': 200,
            'name': 'jobsdb',
            'url': 'https://www.jobsdbnew.com'
        }
        response = self.client.put(
            '/scraper/config/', data=json.dumps(request_body), content_type="application/json")
        self.assertEqual(response.json(), expected_response)

    def test_patch_invalid_body_fail(self):
        expected_response = {
            'message': 'Invalid request'
        }
        request_body = {
            'id': 200,
            'namesss': 'jobsdb',
            'urlsss': 'https://www.jobsdbnew.com'
        }
        response = self.client.put(
            '/scraper/config/', data=json.dumps(request_body), content_type="application/json")
        self.assertEqual(response.json(), expected_response)

    def test_patch_only_name_fail(self):
        expected_response = {
            'message': 'Error creating config'
        }
        request_body = {
            'name': 'jobsdb',
        }
        response = self.client.put(
            '/scraper/config/', data=json.dumps(request_body), content_type="application/json")
        self.assertEqual(response.json(), expected_response)

    def test_delete_valid_config(self):
        expected_response = {
            'id': 1,
            'name': 'jobsdb',
            'url': 'https://www.jobsdb.com'
        }
        response = self.client.delete('/scraper/config/?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_delete_invalid_config(self):
        expected_response = {
            'message': 'id 200 do not exists'
        }
        response = self.client.delete('/scraper/config/?id=200')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)


class TestSyncJob(TestCase):

    @patch('scraper.adapters.kafka_queue.KafkaProducer')
    def test_get_job_sync_valid_id(self, mock_kafka_producer):
        expected_response = {
            'message': 'Started Sync'
        }
        response = self.client.get('/scraper/sync_jobs/?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)


    @patch('scraper.adapters.kafka_queue.KafkaProducer')
    def test_get_job_sync_invalid_id(self, mock_kafka_producer):
        self.assertRaises(
            InvalidScaperId,
            self.client.get,
            '/scraper/sync_jobs/?id=2000'
        )