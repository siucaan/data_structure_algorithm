class ArrQueue:
    """
    使用list实现队列
    """
    def __init__(self):
        self.items = []

    def enque(self, val):
        """
        入队，list的尾为队首
        :param val:
        :return: 无
        """
        self.items.insert(0, val)

    def outque(self):
        """
        出队，返回队首的值，并从队中删除
        :return: 队首值
        """
        return self.items.pop()

    def front(self):
        """
        查看队首值
        :return: 队首值
        """
        if self.items:
            return self.items[len(self.items)-1]
        return None

    def back(self):
        """
        查看队尾值
        :return: 队尾值
        """
        if self.items:
            return self.items[0]
        return None

    def size(self):
        """
        返回队列大小
        :return: 队列大小
        """
        return len(self.items)

    def is_empty(self):
        """
        判断队列是否为空
        :return: bool值
        """
        if self.items:
            return False
        return True


class Node:
    """
    用于实现链表的节点类
    """
    def __init__(self, val=None):
        self.data = val
        self.next = None


class LinkListQueue:
    """
    使用单向链表实现队列
    """
    def __init__(self):
        self.head = Node()
        self.length = 0
        self.tail = self.head  # 定义一个尾指针

    def enque(self, val):
        """
        入队， 队首为链表的头部
        :param val: 入队值
        :return: 无
        """
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def outque(self):
        """
        出队，返回队首值并将其从队中删除
        :return: 队首值
        """
        if self.length:
            tmp = self.head.next
            self.head.next = self.head.next.next
            pop_val = tmp.data
            del tmp
            self.length -= 1
            if not self.length:
                self.tail = self.head
            return pop_val
        return None

    def front(self):
        if self.length:
            return self.head.next.data
        return None

    def back(self):

        return self.tail.data

    def size(self):
        return self.length

    def is_empty(self):
        if self.length:
            return False
        return True


if __name__ == '__main__':
    sample = [1, 2, 4, 8, 16]

    arr_que = ArrQueue()
    print('is empty?', arr_que.is_empty())
    for x in sample:
        arr_que.enque(x)
        print('input', x, 'front element:', arr_que.front(), 'tail element:', arr_que.back())

    print('is empty?', arr_que.is_empty())
    print('front element:', arr_que.front(), 'back element:', arr_que.back())
    print('size:', arr_que.size())
    for _ in sample:
        print('output', arr_que.outque(), 'size:', arr_que.size(), 'front element:', arr_que.front(), 'tail element:', arr_que.back())

    print('**************************')
    print('*** test linklistqueue ***')
    print('**************************')

    ll_que = LinkListQueue()
    print('is empty?', ll_que.is_empty())
    for x in sample:
        ll_que.enque(x)
        print('input', x, 'front element:', 'front element:', ll_que.front(), 'tail element:', ll_que.back())

    print('is empty?', ll_que.is_empty())
    print('front element:', ll_que.front(), 'tail element:', ll_que.back())
    print('size:', ll_que.size())
    for _ in sample:
        print('output', ll_que.outque(), 'size:', ll_que.size(), 'front element:', ll_que.front(), 'tail element:', ll_que.back())
