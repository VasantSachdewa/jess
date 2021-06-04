import json

from jess.libs.logs import Logs
from jess.settings import KAFKA_CONFIG
from kafka import KafkaProducer
from scraper.adapters.queue_interface import QueueInterface
from typing import Any

logger = Logs.get_logger('Scraper')


class KafkaAdapter(QueueInterface):

    KAFKA_CONFIG = KAFKA_CONFIG

    def get_producer(self) -> KafkaProducer:
        return KafkaProducer(
            value_serializer=lambda m: json.dumps(m).encode('ascii'),
            bootstrap_servers=self.KAFKA_CONFIG['KAFKA_HOST'],
            api_version=(0, 10)
        )

    def drop_message(self, message: Any):
        producer = self.get_producer()
        producer.send(
            self.KAFKA_CONFIG['KAFKA_TOPIC'],
            message
        )
        # producer.flush()
