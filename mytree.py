# -*- coding: utf-8 -*-
# @Time    : 2019-07-11 22:43
# @Author  : shaocanfan
# @File    : mytree.py



class BinTree:
    def __init__(self, root_val):
        self.root = root_val
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinTree(value)
        else:
            newnode = BinTree(value)
            newnode.left_child = self.left_child
            self.left_child = newnode


    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinTree(value)
        else:
            newnode = BinTree(value)
            newnode.right_child = self.right_child
            self.right_child = newnode

    def get_root(self):
        return self.root

    def set_root(self, value):
        self.root = value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def pre_order(self):
        print(self.get_root())
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.get_root())
        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.get_root())



def pre_oreder(atree):
    if atree:
        print(atree.get_root())
        pre_oreder(atree.get_left_child())
        pre_oreder(atree.get_right_child())

def post_order(atree):
    if atree:
        post_order(atree.get_left_child())
        print(atree.get_root())
        post_order(atree.get_right_child())

def in_order(atree):
    if atree:
        in_order(atree.get_left_child())
        in_order(atree.get_right_child())
        print(atree.get_root())


if __name__ == "__main__":
    bt = BinTree('root')
    print(bt.get_root())
    bt.insert_left("left child")
    bt.insert_right("right child")
    print(bt.get_left_child().get_root())
    print(bt.get_right_child().get_root())
    bt.set_root("new_root")
    print(bt.get_root())

    print("test inner pre order ...")
    bt.pre_order()
    print("test inner in order ...")
    bt.in_order()
    print("test inner post order ...")
    bt.post_order()

    print("test outter pre order ...")
    pre_oreder(bt)
    print("test outter post order ...")
    post_order(bt)
    print("test outter in order ...")
    in_order(bt)
