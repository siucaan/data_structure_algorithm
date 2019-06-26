# -*- coding: utf-8 -*-
# @Time    : 2019-06-26 20:59
# @Author  : shaocanfan
# @File    : ch2_5.py


from collections import deque


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.seq = 0

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_seq(self):
        return self.seq

    def set_seq(self, s):
        self.seq = s

    def equals(self, arg):
        return self.id == arg.get_id()

    def cur_pos(self):
        return self.id, self.name, self.seq


class MyQueue:
    def __init__(self):
        self.q = deque()

    def en_queue(self, user):
        """入队，q的头部为队首，尾部为队尾"""
        user.set_seq(len(self.q) + 1)
        self.q.append(user)

    def update(self):
        """从头到尾更新用户的当前的次序"""
        i = 1
        for user in self.q:
            user.set_seq(i)
            i += 1

    def de_queue(self):
        """出队并更新当前每个用户的次序"""
        self.q.popleft()
        self.update()

    def random_deq(self, user):
        """队列中用户随机离开，更新用户当前次序"""
        self.q.remove(user)
        self.update()











