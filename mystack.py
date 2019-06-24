class ArrStack:
    """
    使用list实现栈，第一个元素为栈底，最后一个元素为栈顶
    """
    def __init__(self):
        """
        初始化为空list
        """
        self.items = []

    def stackin(self, value):
        """
        入栈
        :param value: 入栈的值
        :return: NULL
        """
        self.items.append(value)

    def stackpop(self):
        """
        出栈，删除栈顶的内容
        :return: 栈顶的值
        """
        return self.items.pop()

    def top(self):
        """
        获取栈顶的值
        :return: 栈顶的值
        """
        if self.items:
            return self.items[len(self.items)-1]
        return None

    def is_empty(self):
        """
        是否为空栈
        :return: bool值
        """
        if self.items:
            return False
        return True

    def size(self):
        """
        获取栈的大小
        :return: 栈的大小
        """
        return len(self.items)


class Node:
    """
    节点，用于实现栈
    """
    def __init__(self, val=None):
        self.data = val
        self.next = None


class LinkListStack:
    """
    单向链表实现栈，第一个节点为栈顶，最后一个节点为栈底
    """
    def __init__(self):
        self.head = Node()
        self.length = 0  # 定义一个长度属性方便size，is_empty等等

    def stackin(self, val):
        new_node = Node(val)
        tmp = self.head.next
        self.head.next = new_node
        new_node.next = tmp
        self.length += 1

    def stackpop(self):
        if not self.length:
            return None
        tmp = self.head.next
        self.head.next = self.head.next.next
        self.length -= 1
        pop_val = tmp.data
        del tmp
        return pop_val

    def top(self):
        if not self.length:
            return None
        return self.head.next.data

    def is_empty(self):
        if self.length:
            return False
        return True

    def size(self):
        return self.length


if __name__ == "__main__":
    arr_stack = ArrStack()
    ll_stack = LinkListStack()
    sample = [1, 2, 3, 4]

    print('arr_stack is empty?', arr_stack.is_empty())
    print('ll_stack is empty?', arr_stack.is_empty())

    for x in sample:
        arr_stack.stackin(x)
        print('input to stack', x, 'arr_stack is empty?', arr_stack.is_empty(), 'size:', arr_stack.size(), 'stack top:',
              arr_stack.stacktop())

    for _ in sample:
        print('pop:', arr_stack.stackpop(), 'arr_stack is empty?', arr_stack.is_empty(), 'size:', arr_stack.size(), 'stack top:', arr_stack.stacktop())

    print('**************************')
    print('*** test linkliststack ***')
    print('**************************')

    for x in sample:
        ll_stack.stackin(x)
        print('input to stack', x, 'll_stack is empty?', ll_stack.is_empty(), 'size:', ll_stack.size(), 'stack top:',
              ll_stack.stacktop())
    for _ in sample:
        print('pop:', ll_stack.stackpop(), 'll_stack is empty?', ll_stack.is_empty(), 'size:', ll_stack.size(), 'stack top:', ll_stack.stacktop())




