from worker.adapters.queue_factory import QueueFactory
from jess.libs.logs import Logs
from worker.extractors.extractor_factory import JobsExtractorFactory
from worker.adapters.datastore_factory import DatastoreFactory
from jess.libs.metrics_tracker import STATSD_CLIENT

import json

logger = Logs.get_logger("Worker")


class SyncJobsController:
    """
    The responsibility of this module is to fetch raw jobs data from
    queue and then extract(clean) it and evntually store it in datastore
    """

    def __init__(self):
        self.db_adapter = DatastoreFactory.get_datastore_adapter()

    # get data from queue
    def store_from_queue_to_datastore(self):
        # Initialize queue
        queue = QueueFactory.get_message_queue()
        # Consume from queue
        for message in queue.consume_message():
            vendor_id = message.value["vendor_id"]
            raw_job_list = message.value["message"]
            logger.debug(
                "Extracting data for vendor_id {} message size {}".format(
                    vendor_id, len(raw_job_list)
                )
            )
            # loop through message job list inside each message
            for job in raw_job_list:
                detail_extractor = JobsExtractorFactory.get_extractor(
                    vendor_id, job
                )
                extracted_job_detail = detail_extractor.get_cleaned_data()
                self.db_adapter.store_jobs_data(
                    vendor_id, extracted_job_detail, job
                )


class SyncJobsControllerSNS: 
    '''
        The responsibility of the module is to extract
        and transform the data recreived from SNS into 
        Datastore 
    '''

    def __init__(self):
        self.db_adapter = DatastoreFactory.get_datastore_adapter()

    @STATSD_CLIENT.timer('worker.SyncJobsControllerSNS.store_data_to_datastore')
    def store_data_to_datastore(self, data: dict):
        for record in data["Records"]:
            logger.debug("Transforming data for {}".format(record))
            parsed_data = json.loads(record['Sns']['Message'])
            vendor_id = parsed_data["vendor_id"]
            raw_job_list = parsed_data["message"]
            logger.debug(
                "Extracting data for vendor_id {} message size {}".format(
                    vendor_id, len(raw_job_list)
                )
            )

            for job in raw_job_list:
                detail_extractor = JobsExtractorFactory.get_extractor(
                    vendor_id, job
                )
                extracted_job_detail = detail_extractor.get_cleaned_data()
                self.db_adapter.store_jobs_data(
                    vendor_id, extracted_job_detail, job
                )
