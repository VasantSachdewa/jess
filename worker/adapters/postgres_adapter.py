from worker.adapters.datastore_interface import DatastoreInterface
from worker.models import JobsRaw, Vendors, JobsDetail
from worker.extractors.extractor_interface import ExtractedDataType
from jess.libs.logs import Logs
from jess.libs.metrics_tracker import STATSD_CLIENT
from typing import Dict

logger = Logs.get_logger("Worker")


class PostgresAdapter(DatastoreInterface):
    @STATSD_CLIENT.timer('worker.PostgresAdapter.store_jobs_data')
    def store_jobs_data(
        self, vendor_id: int, extracted_data: ExtractedDataType, raw_data: Dict
    ) -> JobsDetail:
        vendor_obj = Vendors.objects.get(vendor_id=vendor_id)
        job_details_obj = self.store_extracted_data(vendor_obj, extracted_data)
        self.store_raw_data(job_details_obj, raw_data)

    @STATSD_CLIENT.timer('worker.PostgresAdapter.store_extracted_data')
    def store_extracted_data(
        self, vendor_obj: Vendors, extracted_data: ExtractedDataType
    ) -> JobsDetail:
        logger.debug("Storing {} to Postgres database".format(extracted_data))
        extracted_data["vendor_id"] = vendor_obj
        job_detail_obj, _ = JobsDetail.objects.update_or_create(
            vendor_id=extracted_data["vendor_id"],
            job_id=extracted_data["job_id"],
            defaults={
                "page_url": extracted_data["page_url"],
                "salary_min": extracted_data["salary_min"],
                "salary_max": extracted_data["salary_max"],
                "currency": extracted_data["currency"],
                "job_title": extracted_data["job_title"],
                "company": extracted_data["company"],
                "post_date": extracted_data["post_date"],
                "job_description": extracted_data["job_description"],
                "job_requirements": extracted_data["job_requirements"],
                "benefits": extracted_data["benefits"],
                "industry": extracted_data["industry"]
            }
        )
        logger.debug(
            "Successfully stored data with id {}".format(job_detail_obj.job_id)
        )

        return job_detail_obj

    def store_raw_data(
        self, job_detail_obj: JobsDetail, raw_data: Dict
    ) -> JobsRaw:
        raw_obj, _ = JobsRaw.objects.update_or_create(
            id=job_detail_obj,
            vendor_id=job_detail_obj.vendor_id,
            job_id=job_detail_obj.job_id,
            defaults={"raw_data": raw_data},
        )

        return raw_obj
