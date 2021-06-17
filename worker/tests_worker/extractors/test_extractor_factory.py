import unittest
from worker.extractors.extractor_factory import JobsExtractorFactory
from worker.extractors.jobsdb_extractor import JobsdbDetailExtractor
from worker.extractors.extractor_interface import JobExtractorInterface
from worker.exceptions import InvalidExtractorId


class TestJobsExtractorFactory(unittest.TestCase):

    def test_get_jobsdb_extractor_id_1(self):
        extractor_obj = JobsExtractorFactory.get_extractor(1, {})
        self.assertTrue(isinstance(extractor_obj, JobsdbDetailExtractor))
        self.assertTrue(isinstance(extractor_obj, JobExtractorInterface))

    def  test_get_jobsdb_extractor_invalid_id(self):
        self.assertRaises(InvalidExtractorId, JobsExtractorFactory.get_extractor, 222, {})
