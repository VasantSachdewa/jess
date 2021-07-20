import unittest
from unittest.mock import patch, MagicMock
from worker.controllers.sync_jobs_controller import SyncJobsController


class MockKafkaMessage:
    def __init__(self, vendor_id, message):
        self.value = {"vendor_id": vendor_id, "message": message}


class TestSyncJobsController(unittest.TestCase):
    @patch("worker.controllers.sync_jobs_controller.JobsExtractorFactory")
    @patch("worker.controllers.sync_jobs_controller.DatastoreFactory")
    @patch("worker.controllers.sync_jobs_controller.QueueFactory")
    def test_store_from_queue_to_datastore_valid(
        self, queue_factory, datastore_factory, jobs_extractor_factory
    ):
        # mock queue
        queue_obj = MagicMock()
        queue_obj.consume_message = MagicMock(
            return_value=[MockKafkaMessage("random_id", "random_message")]
        )
        queue_factory.get_message_queue = MagicMock(return_value=queue_obj)
        # mock_extractor
        extractor_obj = MagicMock()
        jobs_extractor_factory.get_extractor = MagicMock(
            return_value=extractor_obj
        )
        # mock datastore factory
        db_adapter_obj = MagicMock()
        datastore_factory.get_datastore_adapter = MagicMock(return_value=db_adapter_obj)

        controller = SyncJobsController()
        controller.store_from_queue_to_datastore()
        self.assertTrue(extractor_obj.get_cleaned_data.called)
        self.assertTrue(db_adapter_obj.store_jobs_data.called)
