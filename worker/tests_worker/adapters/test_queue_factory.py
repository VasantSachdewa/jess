import unittest
from worker.adapters.queue_factory import QueueFactory
from worker.adapters.queue_interface import QueueInterface


class TestQueueFactory(unittest.TestCase):

	def test_get_message_queue(self):
		queue_obj = QueueFactory.get_message_queue()
		self.assertTrue(isinstance(queue_obj, QueueInterface))