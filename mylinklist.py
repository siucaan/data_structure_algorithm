# -*- coding: utf-8 -*-
# @Time    : 2019/6/16 20:41
# @Author  : shaocanfan
# @File    : mylinklist.py


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkList:
    def __init__(self):
        self.length = 0
        self.root = Node()
        self.tail = None

    def iter_node(self):
        cur = self.root.next
        while cur is not self.tail:
            yield cur
            cur = cur.next
        if cur is not None:
            yield cur

    def __iter__(self):
        for node in self.iter_node():
            yield node.data

    def __len__(self):
        return self.length

    def append(self, data):
        new_node = Node(data)
        if not self.length:
            self.root.next = new_node
            self.tail = new_node
            self.length += 1
            return
        tail_node = self.tail
        tail_node.next = new_node
        self.tail = new_node
        self.length += 1
        return

    def arr_to_linklist(self, arr):
        for x in arr:
            self.append(x)

    def reverse(self, ):
        if self.length == 0:
            raise Exception('trying to reverse a empty linked list.')
        if self.length == 1:
            return
        else:
            pre = self.root.next
            cur = pre.next
            nex = cur.next

            pre.next = None
            self.tail = pre
            while cur.next is not None:
                cur.next = pre
                pre = cur
                cur = nex
                nex = nex.next
            cur.next = pre
            self.root.next = cur


def method_1(ll1, ll2):
    res_ll = LinkList()
    ll1_node = ll1.root.next
    ll2_node = ll2.root.next
    finish = False
    c = 0
    while not finish:
        if ll1_node is not None and ll2_node is not None:
            sums = ll1_node.data + ll2_node.data + c
            if sums >= 10:
                sums = sums - 10
                c = 1
            res_ll.append(sums)
            ll1_node = ll1_node.next
            ll2_node = ll2_node.next

        if ll1_node is not None and ll2_node is None:
            sums = ll1_node.data + c
            if sums >= 10:
                sums = sums - 10
                c = 1
                res_ll.append(sums)
                ll1_node = ll1_node.next
            else:
                c = 0
                res_ll.append(sums)
                ll1_node = ll1_node.next
        if ll1_node is None and ll2_node is not None:
            sums = ll2_node.data + c
            if sums >= 10:
                sums = sums - 10
                c = 1
                res_ll.append(sums)
                ll2_node = ll2_node.next
            else:
                c = 0
                res_ll.append(sums)
                ll2_node = ll2_node.next

        if ll1_node is None and ll2_node is None:
            if c:
                res_ll.append(c)
            finish = True
    return res_ll


arr = [3, 4, 5, 6, 7, 8]
ll1 = LinkList()
ll1.arr_to_linklist(arr)
arr = [9, 8, 7, 6, 5]
ll2 = LinkList()
ll2.arr_to_linklist(arr)
res = method_1(ll1, ll2)
for x in res:
    print(x)

