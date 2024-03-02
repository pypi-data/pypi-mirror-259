from typing import Iterable

# from pympler import asizeof
from collections import deque


class Queue:

    def __init__(self):
        self._seed_queue = deque()

    @property
    def queue_names(self):
        return tuple(self.__dict__.keys())

    @property
    def used_memory(self):
        return asizeof.asizeof(self)

    def create_queue(self, queue_name: str):
        self.__setattr__(queue_name, deque())

    def push_seed(self, seed):
        self.push("_seed_queue", seed)

    def pop_seed(self):
        return self.pop("_seed_queue")

    def push(self, queue_name: str, data, left: bool = False):
        try:
            if not data:
                return None
            queue = self.__getattribute__(queue_name)
            if isinstance(data, Iterable):
                queue.extend(data) if left else queue.extendleft(data)
            else:
                queue.appendleft(data) if left else queue.append(data)
        except AttributeError as e:
            print(e)

    def pop(self, queue_name: str, left: bool = True):
        try:
            queue = self.__getattribute__(queue_name)
            return queue.pop() if left else queue.popleft()
        except IndexError as e:
            print(e)
            return None
        except AttributeError as e:
            print(e)
            return None


# qqueue = Queue()
# # qqueue.create_queue("test")
# print(qqueue.queue_names)
# qqueue.push("task_queue", "key")
# print(qqueue.used_memory)
# c = qqueue.pop("task_queue")
# print(c)

