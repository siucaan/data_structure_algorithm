# -*- coding: utf-8 -*-
# @Time    : 2019-06-24 21:37
# @Author  : shaocanfan
# @File    : ch2_3.py


from mystack import ArrStack

def move_botton_top(s):
    if s.is_empty():
        return
    top1 = s.top()
    s.stackpop()
    if not s.is_empty:
        move_botton_top(s)
        top2 = s.top()
        s.stackpop()
        s.stackin(top1)
        s.stackin(top2)
    else:
        s.stackin(top1)

def reverse_stack(s):
    if s.is_empty():
        return
    move_botton_top(s)
    t = s.top()
    s.stackpop()
    reverse_stack(s)
    s.stackin(t)


arr_stack = ArrStack()
sample = [1, 2, 3, 4]

for x in sample:
    arr_stack.stackin(x)
reverse_stack(arr_stack)
while not arr_stack.is_empty():
    print(arr_stack.stackpop())