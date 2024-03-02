# -*- coding: utf-8 -*-

class DynamicHashTable:
    def __init__(self):
        self.capacity = 1000  # 初始容量
        self.size = 0  # 元素个数
        self.table = [None] * self.capacity

    def hash_function(self, key):
        return hash(key) % self.capacity

    def probe(self, index):
        # 线性探测法
        return (index + 1) % self.capacity

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index][1] = value
                return
            index = self.probe(index)
        self.table[index] = [key, value]
        self.size += 1

        # 动态扩容
        if self.size / self.capacity >= 0.7:
            self.resize()

    def get(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = self.probe(index)
        raise KeyError("Key not found")

    def remove(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.size -= 1
                return
            index = self.probe(index)
        raise KeyError("Key not found")

    def resize(self):
        # 扩容为原容量的两倍
        self.capacity *= 2
        new_table = [None] * self.capacity
        for item in self.table:
            if item is not None:
                key, value = item
                new_index = self.hash_function(key)
                while new_table[new_index] is not None:
                    new_index = self.probe(new_index)
                new_table[new_index] = [key, value]
        self.table = new_table

