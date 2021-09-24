from scraper.adapters.queue_factory import QueueFactory
from scraper.adapters.scraper_factory import ScraperFactory
from jess.libs.logs import Logs
from jess.libs.metrics_tracker import STATSD_CLIENT

logger = Logs.get_logger("Scraper")


class JobSyncController:
    def __init__(self, vendor_id: int):
        self.id = vendor_id
        scraper_klss = ScraperFactory.get_adapter(vendor_id)
        self.scraper_adapter = scraper_klss()
        self.queue_adapter = QueueFactory.get_message_queue()

    @STATSD_CLIENT.timer('scraper.JobSyncController.sync_vendor')
    def sync_vendor(self):
        logger.debug("Started syncing for vendor_id {}".format(self.id))
        raw_data = self.scraper_adapter.get_posts()
        message = {"vendor_id": self.id, "message": raw_data}
        self.queue_adapter.drop_message(message)
        logger.debug("Finished syncing for vendor")

        return {"message": "Started Sync"}
