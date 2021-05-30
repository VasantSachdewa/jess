from jess.libs.logs import Logs

logger = Logs.get_logger('Scraper')

class BadRequestException(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        logger.error(message)