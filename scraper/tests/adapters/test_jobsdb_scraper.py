import unittest
import json
from unittest.mock import MagicMock, patch
from scraper.adapters.jobsdb_scraper import JobsdbScraper
from scraper.tests.adapters.test_configs import (
    JOB_LISTINGS,
    JOB_LISTING_ENDPOINT,
    LISTING_REQUEST_BODY,
    JOB_DETAIL_REQUEST_BODY,
    JOB_LISTING_API_RAW_RETURN,
    HEADER,
)


class TestJobsdbScraper(unittest.TestCase):
    @patch("scraper.adapters.jobsdb_scraper.logger")
    @patch("scraper.adapters.jobsdb_scraper.requests")
    @patch("scraper.adapters.jobsdb_scraper.JobsdbScraper.get_job_listings")
    def test_get_job_details_list_valid(
        self, get_job_listings_fn, requests_module, logger_module
    ):
        get_job_listings_fn.return_value = JOB_LISTINGS
        post_response = MagicMock()
        post_response.status_code = 200
        requests_module.post = MagicMock(return_value=post_response)
        scraper = JobsdbScraper()
        job_details_list = scraper.get_job_detail_list(3)
        self.assertEqual(type(job_details_list), list)
        self.assertFalse(logger_module.error.called)
        requests_module.post.assert_called_with(
            url=JOB_LISTING_ENDPOINT,
            data=json.dumps(JOB_DETAIL_REQUEST_BODY),
            headers=HEADER,
        )

    @patch("scraper.adapters.jobsdb_scraper.logger")
    @patch("scraper.adapters.jobsdb_scraper.requests")
    @patch("scraper.adapters.jobsdb_scraper.JobsdbScraper.get_job_listings")
    def test_get_job_details_response_400(
        self, get_job_listings_fn, requests_module, logger_module
    ):
        get_job_listings_fn.return_value = JOB_LISTINGS
        post_response = MagicMock()
        post_response.status_code = 400
        requests_module.post = MagicMock(return_value=post_response)
        scraper = JobsdbScraper()
        job_details_list = scraper.get_job_detail_list(3)
        self.assertEqual(type(job_details_list), list)
        self.assertTrue(logger_module.error.called_once)
        logger_args, kwargs = logger_module.error.call_args
        self.assertTrue("Failed to request job_id" in logger_args[0])

    @patch("scraper.adapters.jobsdb_scraper.logger")
    @patch("scraper.adapters.jobsdb_scraper.requests")
    @patch("scraper.adapters.jobsdb_scraper.JobsdbScraper.get_job_listings")
    def test_get_job_details_response_unexpected_error(
        self, get_job_listings_fn, requests_module, logger_module
    ):
        get_job_listings_fn.return_value = JOB_LISTINGS
        post_response = MagicMock()
        post_response.status_code = 200
        requests_module.post = MagicMock(return_value="")
        scraper = JobsdbScraper()
        job_details_list = scraper.get_job_detail_list(3)
        self.assertEqual(type(job_details_list), list)
        self.assertTrue(logger_module.error.called_once)
        logger_args, kwargs = logger_module.error.call_args
        self.assertTrue("Failed request with error" in logger_args[0])

    @patch("scraper.adapters.jobsdb_scraper.logger")
    @patch("scraper.adapters.jobsdb_scraper.requests")
    def test_get_job_listings_valid(self, requests_module, logger_module):
        post_response = MagicMock()
        post_response.json = MagicMock(return_value=JOB_LISTING_API_RAW_RETURN)
        post_response.status_code = 200
        requests_module.post = MagicMock(return_value=post_response)
        scraper = JobsdbScraper()
        jobs_listings_list = scraper.get_job_listings(2)
        self.assertEqual(type(jobs_listings_list), list)
        self.assertFalse(logger_module.error.called)
        requests_module.post.assert_called_with(
            url=JOB_LISTING_ENDPOINT,
            data=json.dumps(LISTING_REQUEST_BODY),
            headers=HEADER,
        )

    @patch("scraper.adapters.jobsdb_scraper.logger")
    @patch("scraper.adapters.jobsdb_scraper.requests")
    def test_get_job_listings_response_400(
        self, requests_module, logger_module
    ):
        post_response = MagicMock()
        post_response.status_code = 400
        requests_module.post = MagicMock(return_value=post_response)
        scraper = JobsdbScraper()
        job_details_list = scraper.get_job_listings(3)
        self.assertEqual(type(job_details_list), list)
        self.assertTrue(logger_module.error.called_once)
        logger_args, kwargs = logger_module.error.call_args
        self.assertTrue("Failed request for page_number" in logger_args[0])
        self.assertFalse("Failed request with error" in logger_args[0])

    @patch("scraper.adapters.jobsdb_scraper.logger")
    @patch("scraper.adapters.jobsdb_scraper.requests")
    def test_get_job_listings_response_unexpected_error(
        self, requests_module, logger_module
    ):
        post_response = MagicMock()
        post_response.status_code = 200
        requests_module.post = MagicMock(return_value="")
        scraper = JobsdbScraper()
        job_details_list = scraper.get_job_listings(3)
        self.assertEqual(type(job_details_list), list)
        self.assertTrue(logger_module.error.called_once)
        logger_args, kwargs = logger_module.error.call_args
        self.assertTrue("Failed request with error" in logger_args[0])


if __name__ == "__main__":
    unittest.main()
