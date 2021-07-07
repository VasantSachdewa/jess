import json

from jess.libs.logs import Logs
from jess.settings import KAFKA_CONFIG
from kafka import KafkaProducer
from scraper.adapters.queue_interface import QueueInterface
from typing import Any

logger = Logs.get_logger("Scraper")


class KafkaAdapter(QueueInterface):

    KAFKA_CONFIG = KAFKA_CONFIG
    CHUNK_SIZE = 10

    def get_producer(self) -> KafkaProducer:
        return KafkaProducer(
            value_serializer=lambda m: json.dumps(m).encode("ascii"),
            bootstrap_servers=self.KAFKA_CONFIG["KAFKA_HOST"],
            api_version=(0, 10),
        )

    def drop_message(self, messages: Any):
        producer = self.get_producer()
        for message in self._get_chunk(messages):
            producer.send(self.KAFKA_CONFIG["KAFKA_TOPIC"], message)
            producer.flush()

    def _get_chunk(self, messages):
        for i in range(0, len(messages["message"]), self.CHUNK_SIZE):
            yield {
                "vendor_id": messages["vendor_id"],
                "message": messages["message"][i : i + self.CHUNK_SIZE],
            }
