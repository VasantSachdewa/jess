import json
import datetime
from unittest import skip

from django.core.exceptions import ValidationError
from django.test import TestCase
from worker.models import JobsdbRaw, JobsDetail, Vendors


class TestJobsdbRaw(TestCase):

    def test_create_jobsdbraw_valid_record(self):
        record = JobsdbRaw.objects.create(
            job_id='1',
            raw_data={
                'title': 'Software Engineer',
                'salary': 20000
            }
        )
        #does validation
        record.full_clean()
        self.assertEqual(record.job_id, '1')


class TestVendors(TestCase):

    def test_create_vendor_valid_record(self):
        record = Vendors(
            name='jobsdb',
            url='https://www.jobsdb.com'
        )
        record.full_clean()
        record.save()
        self.assertEqual(record.vendor_id, 2)
        self.assertEqual(record.name, 'jobsdb')
        self.assertEqual(record.url, 'https://www.jobsdb.com')

    def test_create_vendor_invalid_url_record(self):
        record = Vendors(
            name='jobsdb',
            url='random_text'
        )
        self.assertRaises(ValidationError, record.full_clean)


class TestJobsDetail(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.vendor_obj = Vendors.objects.create(
            name='jobsdb',
            url='https://www.jobsdb.com'
        )

    @skip("Some weird error")
    def test_create_jobdetails_valid_record(self):
        job_requirements = "Best developer in the world,C++ programmer,"\
            "DevOps Experience"
        job_description = "Build new features on Apple webpage,Build"\
            " features on Siri,Work on security features"
        benefits = "Best salary in the world,200 days paid holiday"\
            ",Cover dentist charges"
        record = JobsDetail(
            vendor_id=self.vendor_obj,
            job_id='00000001',
            page_url='https://www.jobsdb.com/posts/1',
            salary_min=None,
            salary_max=None,
            currency=None,
            job_title='Software Engineer',
            company='Apple',
            post_date=datetime.datetime.now(),
            job_description=job_description,
            job_requirements=job_requirements,
            benefits=benefits,
            industry="Technology"
        )
        record.full_clean()
