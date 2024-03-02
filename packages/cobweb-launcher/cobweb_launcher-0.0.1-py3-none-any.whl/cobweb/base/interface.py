import json
from abc import ABC, abstractmethod


def parse_config(config):
    if not config:
        return None
    if isinstance(config, str):
        return json.loads(config)
    if isinstance(config, dict):
        return config
    raise TypeError("config type is not in [string, dict]!")


class SchedulerInterface(ABC):

    def __init__(self, table, sql, length, size, queue, config=None):
        self.sql = sql
        self.table = table
        self.length = length
        self.size = size
        self.queue = queue
        self.config = parse_config(config)
        self.stop = False

    @abstractmethod
    def schedule(self, *args, **kwargs):
        pass


class StorerInterface(ABC):

    def __init__(self, table, fields, length, queue, config=None):
        self.table = table
        self.fields = fields
        self.length = length
        self.queue = queue
        self.config = parse_config(config)
        # self.redis_db = redis_db

    @abstractmethod
    def store(self, *args, **kwargs):
        pass

