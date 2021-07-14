import logging
import sys
from jess.settings import LOG_LEVEL_ENV, ENV

LOG_LEVEL = getattr(logging, LOG_LEVEL_ENV)


class Logs:

    __instance = None
    log_level = LOG_LEVEL
    env = ENV

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
        if self.env == 'development':
            #add sys_out handler
            self._setup_sys_out(logger)

        return logger

    def _setup_sys_out(self, logger: logging.Logger) -> None:
        sys_out_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(sys_out_handler)
