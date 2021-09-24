import statsd
from jess.settings import STATSD_HOST, STATSD_PORT


STATSD_CLIENT = statsd.StatsClient(STATSD_HOST, STATSD_PORT)
