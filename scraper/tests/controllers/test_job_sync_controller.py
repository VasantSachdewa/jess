import unittest
from unittest.mock import patch, MagicMock
from scraper.controllers.job_sync_controller import JobSyncController


class TestJobSyncController(unittest.TestCase):

    @patch('scraper.controllers.job_sync_controller.QueueFactory')
    @patch('scraper.controllers.job_sync_controller.ScraperFactory')
    def test_sync_vendor_valid(self, scraper_factory, queue_factory):
        adapter_obj = self._mock_scraper_factory(scraper_factory)
        queue_obj = self._mock_queue_factory(queue_factory)
        controller = JobSyncController(1)
        controller.sync_vendor()
        self.assertTrue(adapter_obj.get_posts.called)
        self.assertTrue(queue_obj.drop_message.called)

    def _mock_scraper_factory(self, scraper_factory):
        adapter_obj = MagicMock()
        adapter = MagicMock(return_value=adapter_obj)
        scraper_factory.get_adapter = MagicMock(return_value=adapter)

        return adapter_obj

    def _mock_queue_factory(self, queue_factory):
        queue_obj = MagicMock()
        queue_factory.get_message_queue = MagicMock(return_value=queue_obj)

        return queue_obj

