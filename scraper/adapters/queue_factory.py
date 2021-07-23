from jess.settings import ENV
from scraper.adapters.queue_interface import QueueInterface


class QueueFactory:
    @staticmethod
    def get_message_queue() -> QueueInterface:
        if ENV == 'production':
            from scraper.adapters.sns_queue import SNSAdapter
            return SNSAdapter()
        else:
            from scraper.adapters.kafka_queue import KafkaAdapter
            return KafkaAdapter()
