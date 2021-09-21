import unittest
from unittest.mock import MagicMixin, patch, MagicMock
from jess.libs.metrics_tracker import counter


class TestMetricsTracker(unittest.TestCase):

	@patch('jess.libs.metrics_tracker.CLOUDWATCH_CLIENT')
	@patch('jess.libs.metrics_tracker.boto3')
	def test_counter(self, boto3_module, client):

		random_func = lambda x: x
		counter('test_function')(random_func)('arg')	

		self.assertTrue(client.put_metric_data.called)