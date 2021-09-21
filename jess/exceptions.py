from jess.libs.logs import Logs

logger = Logs.get_logger("Jess")

class MetricException(Exception):
    
    def __init__(self, error_message):
        logger.debug("Error description: {}".format(error_message))
        super.__init__(error_message)