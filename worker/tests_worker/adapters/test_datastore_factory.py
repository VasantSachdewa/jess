import unittest
from worker.adapters.datastore_factory import DatastoreFactory
from worker.adapters.datastore_interface import DatastoreInterface


class TestDatastoreFactory(unittest.TestCase):
	def test_get_datastore_adapter(self):
		datastore_obj = DatastoreFactory.get_datastore_adapter()
		self.assertTrue(isinstance(datastore_obj, DatastoreInterface))
