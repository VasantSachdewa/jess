import json

from jess.libs.logs import Logs
from jess.settings import KAFKA_CONFIG
from scraper.adapters.queue_interface import QueueInterface
from confluent_kafka import Producer, KafkaError
from typing import Any

logger = Logs.get_logger("Scraper")


class KafkaAdapter(QueueInterface):

    KAFKA_CONFIG = KAFKA_CONFIG
    CHUNK_SIZE = 10

    def get_producer(self):
        kafka = Producer({
            'bootstrap.servers': KAFKA_CONFIG['KAFKA_HOST'],
            'security.protocol': 'SASL_SSL',
            'sasl.mechanisms': 'PLAIN',
            'sasl.username': KAFKA_CONFIG['KAFKA_USERNAME'],
            'sasl.password': KAFKA_CONFIG['KAFKA_PASSWORD'],
            'session.timeout.ms': 45000
        })

        return kafka
    
    def acked(self, err, msg): 
        if (err):
            logger.error('Failed to deliver message: {}'.format(err))
        else:
            logger.info('Dropped record to topic {} partition[{}] @offset {}'.format(
                msg.topic(), msg.partition(), msg.offset()
            ))

    def drop_message(self, messages: Any):
        producer = self.get_producer()
        for message in self._get_chunk(messages):
            producer.produce(self.KAFKA_CONFIG["KAFKA_TOPIC"], value=json.dumps(message), on_delivery=self.acked)
            producer.poll(0)
            producer.flush()

    def _get_chunk(self, messages):
        for i in range(0, len(messages["message"]), self.CHUNK_SIZE):
            yield {
                "vendor_id": messages["vendor_id"],
                "message": messages["message"][i : i + self.CHUNK_SIZE],
            }
