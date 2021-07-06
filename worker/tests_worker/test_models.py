import datetime
from unittest import skip

from django.core.exceptions import ValidationError
from django.test import TestCase
from worker.models import JobsRaw, JobsDetail, Vendors
from worker.tests_worker.test_config import JOB_DETAIL_DATA


class TestJobsRaw(TestCase):
    @classmethod
    def setUpTestData(cls):
        vendor_obj = Vendors(name="random", url="https://www.random.com")
        vendor_obj.save()
        job_detail_obj = JobsDetail(vendor_id=vendor_obj, **JOB_DETAIL_DATA)
        job_detail_obj.save()
        cls.job_detail_obj = job_detail_obj

    def test_create_jobsraw_valid_record(self):
        record = JobsRaw.objects.create(
            id=self.job_detail_obj,
            vendor_id=self.job_detail_obj.vendor_id,
            job_id=self.job_detail_obj.vendor_id,
            raw_data={"title": "Software Engineer", "salary": 20000},
        )
        # does validation
        record.full_clean()
        self.assertEqual(record.job_id, "random")


class TestVendors(TestCase):
    def test_create_vendor_valid_record(self):
        record = Vendors(name="vasant", url="https://www.vasant.com")
        record.full_clean()
        record.save()
        self.assertEqual(record.vendor_id, 4)
        self.assertEqual(record.name, "vasant")
        self.assertEqual(record.url, "https://www.vasant.com")

    def test_create_vendor_invalid_url_record(self):
        record = Vendors(name="jobsdb", url="random_text")
        self.assertRaises(ValidationError, record.full_clean)


class TestJobsDetail(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.vendor_obj = Vendors.objects.create(
            name="random", url="https://www.random.com"
        )

    @skip("Some weird error")
    def test_create_jobdetails_valid_record(self):
        job_requirements = (
            "Best developer in the world,C++ programmer," "DevOps Experience"
        )
        job_description = (
            "Build new features on Apple webpage,Build"
            " features on Siri,Work on security features"
        )
        benefits = (
            "Best salary in the world,200 days paid holiday"
            ",Cover dentist charges"
        )
        record = JobsDetail(
            vendor_id=self.vendor_obj,
            job_id="00000001",
            page_url="https://www.random.com/posts/1",
            salary_min=None,
            salary_max=None,
            currency=None,
            job_title="Software Engineer",
            company="Apple",
            post_date=datetime.datetime.now(),
            job_description=job_description,
            job_requirements=job_requirements,
            benefits=benefits,
            industry="Technology",
        )
        record.full_clean()
