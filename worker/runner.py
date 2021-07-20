import django
django.setup()

from worker.controllers.sync_jobs_controller import SyncJobsControllerSNS


def worker(event, context):
	syncer = SyncJobsControllerSNS()
	syncer.store_data_to_datastore(event)
