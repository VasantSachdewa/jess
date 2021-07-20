import django
django.setup()

from scraper.controllers.job_sync_controller import JobSyncController
from scraper.models import Websites
from jess.libs.logs import Logs
import schedule
import time

logger = Logs.get_logger("Scraper")


def controllers() -> JobSyncController:
	query_set = Websites.objects.all()
	for website_obj in query_set:
		yield JobSyncController(website_obj.id)


def sync_vendors(event=None, context=None):
	'''
		Get list of vendors	and start
		syncing
		arguments event and context are default
		for lambda function
	'''
	for controller in controllers():
		controller.sync_vendor()


if __name__ == '__main__':
	sync_vendors()


