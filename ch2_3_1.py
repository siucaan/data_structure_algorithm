# -*- coding: utf-8 -*-
# @Time    : 2019-06-25 21:47
# @Author  : shaocanfan
# @File    : ch2_3_1.py

from mystack import ArrStack


def move_to_top(s):
    if s.is_empty():
        return
    top1 = s.top()
    s.stackpop()
    if not s.is_empty():
        move_to_top(s)
        top2 = s.top()
        # 当pop出的栈顶元素大于子栈顶元素，则交换
        if top1 > top2:
            s.stackpop()
            s.stackin(top1)
            s.stackin(top2)
            return
    s.stackin(top1)


def sort_stack(s):
    if s.is_empty():
        return
    move_to_top(s)
    t = s.top()
    s.stackpop()
    sort_stack(s)
    s.stackin(t)


arr_stack = ArrStack()
sample = [3, 1, 4, 5, 2]

for x in sample:
    arr_stack.stackin(x)
sort_stack(arr_stack)

while not arr_stack.is_empty():
    print(arr_stack.stackpop())
