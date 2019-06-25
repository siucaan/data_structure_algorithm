# -*- coding: utf-8 -*-
# @Time    : 2019-06-25 22:34
# @Author  : shaocanfan
# @File    : ch2_4.py

from mystack import ArrStack

s = ArrStack()
push_list = [1, 2, 3, 4, 5]
pop_list = [3, 2, 5, 4, 1]
i = 0
for idx, x in enumerate(push_list):
    if s.top() != pop_list[i]:
        s.stackin(x)
    else:
        s.stackpop()
        i += 1
if i < len(pop_list)-1:
    print('False')
elif s.is_empty() and i == len(pop_list)-1:
    print('True')

