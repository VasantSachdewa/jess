import json

from jess.libs.logs import Logs
from jess.settings import KAFKA_CONFIG
from kafka import KafkaConsumer
from worker.adapters.queue_interface import QueueInterface

logger = Logs.get_logger("Worker")


class KafkaAdapter(QueueInterface):

    KAFKA_CONFIG = KAFKA_CONFIG
    GROUP_ID = "WORKER"

    def get_consumer(self) -> KafkaConsumer:
        return KafkaConsumer(
            self.KAFKA_CONFIG["KAFKA_TOPIC"],
            group_id=self.GROUP_ID,
            bootstrap_servers=self.KAFKA_CONFIG["KAFKA_HOST"],
            value_deserializer=lambda m: json.loads(m.decode("ascii")),
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            api_version=(0, 10)
        )

    def consume_message(self):
        return self.get_consumer()
