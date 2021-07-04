from worker.adapters.datastore_interface import DatastoreInterface
from worker.models import JobsRaw, Vendors, JobsDetail
from worker.extractors.extractor_interface import ExtractedDataType
from jess.libs.logs import Logs
from typing import Dict
import json

logger = Logs.get_logger("Worker")


class PostgresAdapter(DatastoreInterface):
    def store_jobs_data(
        self, vendor_id: int, extracted_data: ExtractedDataType, raw_data: Dict
    ) -> JobsDetail:
        vendor_obj = Vendors.objects.get(vendor_id=vendor_id)
        job_details_obj = self.store_extracted_data(vendor_obj, extracted_data)
        raw_obj = self.store_raw_data(job_details_obj, raw_data)

    def store_extracted_data(
        self, vendor_obj: Vendors, extracted_data: ExtractedDataType
    ) -> JobsDetail:
        logger.debug("Storing {} to Postgres database".format(extracted_data))
        extracted_data["vendor_id"] = vendor_obj
        job_detail_obj, _ = JobsDetail.objects.update_or_create(**extracted_data)
        logger.debug(
            "Successfully stored data with id {}".format(job_detail_obj.job_id)
        )

        return job_detail_obj

    def store_raw_data(self, job_detail_obj: JobsDetail, raw_data: Dict) -> JobsRaw:
        raw_obj, _ = JobsRaw.objects.update_or_create(
            id=job_detail_obj,
            vendor_id=job_detail_obj.vendor_id,
            job_id=job_detail_obj.job_id,
            defaults={"raw_data": raw_data},
        )

        return raw_obj
