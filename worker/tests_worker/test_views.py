from worker.tests_worker.test_config import JOB_DETAIL_DATA
from django.test import TestCase
from unittest import mock
import pytest
import sys

try:
    argument = sys.argv[1]
except IndexError:
    argument = None

if argument == "test":
    # check if integration test
    from worker.models import JobsDetail, Vendors

EXPECTED_LIST_RESPONSE = {
    "count": 1,
    "next": None,
    "previous": None,
    "results": [
        {
            "url": mock.ANY,
            "id": mock.ANY,
            "vendor_id": mock.ANY,
            "job_id": "random_id",
            "page_url": "https://www.random.com",
            "salary_min": None,
            "salary_max": None,
            "currency": None,
            "job_title": "Software Engineer",
            "company": "Random limited",
            "post_date": "2021-07-03T17:57:44.942851+07:00",
            "job_description": [
                "Best developer in the world",
                "C++ programmer,DevOps Experience",
            ],
            "job_requirements": [
                "Build new features on Apple webpage",
                "Build features on Siri",
                "Work on security features",
            ],
            "benefits": [
                "Best salary in the world",
                "200 days paid holiday",
                "Cover dentist charges",
            ],
            "industry": "Technology",
        }
    ],
}


@pytest.mark.integration_test
class TestJobDetailVewSet(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        vendor_obj = Vendors(name="random", url="https://www.random.com")
        vendor_obj.save()
        job_detail_obj = JobsDetail(vendor_id=vendor_obj, **JOB_DETAIL_DATA)
        job_detail_obj.save()
        cls.job_detail_obj = job_detail_obj

    def test_list_jobs_valid(self) -> None:
        expected_response = EXPECTED_LIST_RESPONSE
        response = self.client.get(
            "/jobs/", header={"content-type": "application/json"}
        )
        self.assertEqual(response.json(), expected_response)
        self.assertEqual(response.status_code, 200)
