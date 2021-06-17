import sys, os, django
# sys.path.append("/Users/vasant/Desktop/development/job_scanner/jess") #here store is root folder(means parent).
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jess.settings")
django.setup()
from worker.controllers.sync_jobs_controller import SyncJobsController


worker = SyncJobsController()
worker.store_from_queue_to_datastore()