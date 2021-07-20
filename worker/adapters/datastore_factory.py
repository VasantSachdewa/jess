from worker.adapters.postgres_adapter import PostgresAdapter
from worker.adapters.datastore_interface import DatastoreInterface


class DatastoreFactory:
	@staticmethod
	def get_datastore_adapter() -> DatastoreInterface:
		return PostgresAdapter()