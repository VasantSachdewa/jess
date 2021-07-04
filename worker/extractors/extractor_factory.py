from worker.extractors.extractor_interface import (
    JobExtractorInterface,
    ExtractedDataType,
)
from worker.extractors.jobsdb_extractor import JobsdbDetailExtractor
from worker.exceptions import InvalidExtractorId
from typing import Dict


EXTRACTORS = [JobsdbDetailExtractor]


class JobsExtractorFactory:

    __instance = None
    EXTRACTORS = EXTRACTORS

    def __init__(self, _id: int) -> Dict:
        self.extractor_map = {}
        for extractor in EXTRACTORS:
            self.extractor_map[extractor.ID] = extractor
        JobsExtractorFactory.__instance = self

    @staticmethod
    def get_extractor(_id: int, data: ExtractedDataType) -> JobExtractorInterface:
        if not JobsExtractorFactory.__instance:
            JobsExtractorFactory(_id)
        try:
            extractor_klss = JobsExtractorFactory.__instance.extractor_map[_id]
            obj = extractor_klss(data)
        except KeyError as e:
            raise InvalidExtractorId(_id)

        return obj
