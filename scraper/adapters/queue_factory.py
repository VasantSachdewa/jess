from scraper.adapters.kafka_queue import KafkaAdapter
from scraper.adapters.sns_queue import SNSAdapter
from scraper.adapters.queue_interface import QueueInterface


class QueueFactory:
    @staticmethod
    def get_message_queue() -> QueueInterface:
        return SNSAdapter()
