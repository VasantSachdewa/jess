import unittest
from unittest.mock import MagicMock, patch
from worker.adapters.postgres_adapter import PostgresAdapter
from worker.models import JobsDetail, Vendors
from worker.tests_worker.test_config import JOB_DETAIL_DATA


class TestPostgresAdapter(unittest.TestCase):

	@patch('worker.adapters.postgres_adapter.PostgresAdapter.store_raw_data')
	@patch('worker.adapters.postgres_adapter.PostgresAdapter.store_extracted_data')
	@patch('worker.adapters.postgres_adapter.Vendors')
	def test_store_jobs_data_valid(
			self, vendor_model, store_extracted_fn, store_raw_fn):
		vendor_obj = MagicMock()
		vendor_model.objects.get = MagicMock(return_value=vendor_obj)
		vendor_id = 1
		extracted_data = JOB_DETAIL_DATA
		raw_data = {'data': 'all the fields from raw'}
		adapter = PostgresAdapter()
		adapter.store_jobs_data(vendor_id, extracted_data, raw_data)
		self.assertTrue(vendor_model.objects.get.called_with(vendor_obj))
		self.assertTrue(store_extracted_fn.called_with(
			vendor_obj, extracted_data))
		self.assertTrue(store_raw_fn.called_with(vendor_obj, raw_data))

	@patch('worker.adapters.postgres_adapter.JobsDetail')
	def test_store_extracted_data_valid(self, jobs_detail_model): 
		job_detail_obj = MagicMock()
		job_detail_obj.job_id = 'random_id'
		update_or_create_fn = MagicMock(return_value=(job_detail_obj, 'irrelevant'))
		objects_attr = MagicMock()
		objects_attr.update_or_create = update_or_create_fn
		jobs_detail_model.objects = objects_attr
		vendor_obj = Vendors(name='vasant', url='https://www.vasant.com')
		extracted_data = JOB_DETAIL_DATA
		adapter = PostgresAdapter()
		adapter.store_extracted_data(vendor_obj, extracted_data)
		self.assertTrue(update_or_create_fn.called_with(extracted_data))

	@patch('worker.adapters.postgres_adapter.JobsRaw')
	def test_store_raw_data_valid(self, job_raw_model):
		vendor_obj = Vendors(name='vasant', url='https://www.vasant.com')
		JOB_DETAIL_DATA['vendor_id'] = vendor_obj
		job_detail_obj = JobsDetail(**JOB_DETAIL_DATA)
		raw_data = {'data': 'All fields from raw data'}
		update_or_create_fn = MagicMock(return_value=('tup_1', 'tup_2'))
		objects_attr = MagicMock()
		objects_attr.update_or_create = update_or_create_fn
		job_raw_model.objects = objects_attr
		adapter = PostgresAdapter()
		adapter.store_raw_data(job_detail_obj, raw_data)
		self.assertTrue(update_or_create_fn.called_with(
			id=job_detail_obj,
			vendor_id=vendor_obj,
			job_id=job_detail_obj.job_id,
			raw_data=raw_data
		))



		
