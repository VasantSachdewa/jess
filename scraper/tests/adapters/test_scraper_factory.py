from scraper.adapters.scraper_factory import ScraperFactory
from scraper.adapters.jobsdb_scraper import JobsdbScraper
from scraper.exceptions import InvalidScaperId
import unittest


class TestScraperFactory(unittest.TestCase):
    def test_get_adapter_jobsdb_id_valid(self):
        expected_adapter = JobsdbScraper
        adapter = ScraperFactory.get_adapter(1)
        self.assertEqual(expected_adapter, adapter)

    def test_get_adapter_jobsdb_id_invalid(self):
        self.assertRaises(InvalidScaperId, ScraperFactory.get_adapter, 5)
