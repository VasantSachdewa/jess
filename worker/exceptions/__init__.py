from jess.libs.logs import Logs
from typing import Any

logger = Logs.get_logger('Worker')


class InvalidExtractorId(Exception):

    def __init__(self, extractor_id: Any):
        message = 'Invalid extractor id {}'.format(extractor_id)
        logger.error(message)
        super().__init__(message)
