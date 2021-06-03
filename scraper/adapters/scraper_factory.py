from scraper.adapters.job_scraper_interface import JobScraperInterface
from scraper.adapters.jobsdb_scraper import JobsdbScraper
from scraper.exceptions import InvalidScaperId 
from typing import Dict

SCRAPER_ADAPTERS = [
    JobsdbScraper
]


class ScraperFactory:

    __instance = None
    ADAPTERS = SCRAPER_ADAPTERS

    def __init__(self, _id: int) -> Dict:
        self.adapters_map = {}
        for adapter in self.ADAPTERS:
            self.adapters_map[adapter._ID] = adapter
        ScraperFactory.__instance = self

    @staticmethod
    def get_adapter(_id: int) -> JobScraperInterface:
        if not ScraperFactory.__instance:
            ScraperFactory(_id)
        try:
            adapter = ScraperFactory.__instance.adapters_map[_id]
        except KeyError as e:
            raise InvalidScaperId(_id)

        return adapter



