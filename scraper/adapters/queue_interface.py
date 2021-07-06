class QueueInterface:
    def drop_message(self, *args, **kwargs):
        raise NotImplementedError

    def consume_message(self, *args, **kwargs):
        raise NotImplementedError
