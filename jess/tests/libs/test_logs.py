import unittest
from jess.libs.logs import Logs
import logging


class TestLogs(unittest.TestCase):
    def test_get_logger_return_logging_object(self):
        logger = Logs.get_logger("Test")
        self.assertEqual(type(logger), logging.Logger)

    def test_get_logger_promise_singleton(self):
        logger1 = Logs.get_logger("Test")
        logger2 = Logs.get_logger("Test")

        self.assertTrue(logger1 is logger2)


if __name__ == "__main__":
    unittest.main()
