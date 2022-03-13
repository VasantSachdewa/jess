from jess.settings import ENV
from scraper.adapters.queue_interface import QueueInterface


class QueueFactory:
    @staticmethod
    def get_message_queue() -> QueueInterface:
            from scraper.adapters.kafka_queue import KafkaAdapter
            return KafkaAdapter()
