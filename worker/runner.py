import django
django.setup()

from worker.controllers.sync_jobs_controller import SyncJobsControllerSNS
from jess.libs.metrics_tracker import STATSD_CLIENT

@STATSD_CLIENT.timer('worker.worker')
def worker(event, context):
	syncer = SyncJobsControllerSNS()
	syncer.store_data_to_datastore(event)
