import json

from jess.libs.logs import Logs
from jess.settings import SNS_CONFIG
import boto3
from scraper.adapters.queue_interface import QueueInterface
from typing import Dict

logger = Logs.get_logger("Scraper")


class SNSAdapter(QueueInterface):

	SNS_CONFIG = SNS_CONFIG
	CHUNK_SIZE = 5

	def get_producer(self):
		sns_resource = boto3.resource('sns')
		logger.debug("Setting up SNS connection queue id {}".format(
			self.SNS_CONFIG['SNS_HOST']))
		topic = sns_resource.Topic(arn=self.SNS_CONFIG['SNS_HOST'])

		return topic

	def drop_message(self, messages: Dict):
		producer = self.get_producer()
		for message in self._get_chunk(messages):
			logger.debug("Publishing message {}".format(message))
			resp = producer.publish(Message=(json.dumps(message)))
			logger.debug("Successful publish with message_id {}".format(
				resp['MessageId']))

	def _get_chunk(self, messages):
		for i in range(0, len(messages['message']), self.CHUNK_SIZE):
			yield {
				"vendor_id": messages["vendor_id"],
				"message": messages['message'][i : i + self.CHUNK_SIZE]
			}

