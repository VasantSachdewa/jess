from jess.libs.logs import Logs
from typing import Any

logger = Logs.get_logger("Scraper")


class InvalidScaperId(Exception):
    def __init__(self, scraper_id: Any):
        message = "Invalid scraper id {}".format(scraper_id)
        logger.error(message)
        super().__init__(message)
