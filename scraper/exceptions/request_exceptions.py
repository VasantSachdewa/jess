from jess.libs.logs import Logs

logger = Logs.get_logger('Scraper')

class BadRequestException(Exception):

    def __init__(self, message: str) -> None:
        logger.error(message)
        super().__init__(message)


class JobRequestError(Exception):

    def __init__(self, endpoint: str, status_code: int, resp: str):
        message = "Made request to {} with status_code {} with resp {}".format(
            endpoint, status_code, resp)   
        logger.error(message)
        super().__init__(message)


class JobsdbListingRequestError(JobRequestError):
    pass


class JobsdbDetailRequestError(JobRequestError):
    pass