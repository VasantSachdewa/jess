from worker.adapters.kafka_queue import KafkaAdapter
from worker.adapters.queue_interface import QueueInterface


class QueueFactory:
    @staticmethod
    def get_message_queue() -> QueueInterface:
        return KafkaAdapter()
