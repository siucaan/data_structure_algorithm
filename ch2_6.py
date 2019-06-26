# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 21:45
# @Author  : shaocanfan
# @File    : ch2_6.py

from collections import deque

class LRU:
    def __init__(self, size):
        """使用队列和哈希表实现"""
        self.cache_size = size
        self.deq = deque()
        self.hashset = set()

    def is_full(self):
        return self.cache_size == len(self.deq)

    def en_queue(self, page):
        """入队，deq的头部为队首，尾部为队尾"""
        if self.is_full():
            self.hashset.remove(self.deq[-1])
            self.deq.pop()
        self.deq.appendleft(page)
        self.hashset.add(page)

    def access_page(self, page):
        """访问时将对应的任务放到队首"""
        if page not in self.hashset:
            self.en_queue(page)
        else:
            self.deq.remove(page)
            self.deq.appendleft(page)