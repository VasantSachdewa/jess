import unittest

from worker.extractors.jobsdb_extractor import JobsdbDetailExtractor
from worker.tests_worker.extractors.test_configs import (JOBSDB_EXPECTED_DATA,
                                                         JOBSDB_RAW_DATA)


class TestJobsdbDetailExtractor(unittest.TestCase):

    def test_get_cleaned_data_valid(self):
        extractor = JobsdbDetailExtractor(JOBSDB_RAW_DATA)
        extracted_data = extractor.get_cleaned_data()
        self.assertEqual(JOBSDB_EXPECTED_DATA, extracted_data)

