import logging
from jess.settings import LOG_LEVEL_ENV

LOG_LEVEL = getattr(logging, LOG_LEVEL_ENV)


class Logs:

    __instance = None
    log_level = LOG_LEVEL

    def __init__(self, logger_name: str = "SCRAPER") -> None:
        self.logger = self._get_logger_object(logger_name)
        Logs.__instance = self

    @staticmethod
    def get_logger(logger_name: str = "SCRAPER") -> logging.Logger:
        if not Logs.__instance:
            Logs()
        return Logs.__instance.logger

    def _get_logger_object(self, logger_name: str) -> logging.Logger:
        logger = logging.getLogger(logger_name)
        logger.setLevel(self.log_level)

        return logger
