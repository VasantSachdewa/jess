
class QueueInterface():

    def drop_message(self, *args, **kwargs):
        raise NotImplemented

    def consume_message(self, *args, **kwargs):
        raise NotImplemented