class Node(object):
    """单个节点"""
    def __init__(self, item):
        self.elem = item
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        if cur.next == self.__head:
            return 1
        else:
            count = 0
            while cur.next != self.__head:
                count += 1
                cur = cur.next
            return count + 1

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        print(cur.elem)

    def add(self, item):
        """从头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        # 循环结束后，cur指向尾节点
        cur.next = node
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """在尾部插入节点"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        cur.next = node
        node.next = self.__head

    def insert(self, pos, item):
        """在指定位置前插入节点"""
        if self.is_empty():
            node = Node(item)
            self.__head = node
            node.next = node
            return
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            node = Node(item)
            count = 1
            cur = self.__head
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def search(self, item):
        """寻找目标元素"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环后，cur指向最后一个节点，所以还得对最后一个节点的元素进行判断
        if cur.elem == item:
            return True
        return False

    def remove(self, item):
        """删除指定元素；特殊情况：空链表，只有一个节点，要删除的是头节点，要删除的是尾节点"""
        if self.is_empty():
            return
        elif self.length() == 1:    # 针对只有一个节点的情况
            cur = self.__head
            if cur.elem == item:
                self.__head = None
        else:
            cur = self.__head
            pre = None
            while cur.next != self.__head:
                if cur.elem == item:
                    # 针对删除头节点的情况
                    if cur == self.__head:
                        rear = self.__head    # 为了寻找到尾节点，以进一步指向cur的下一个节点形成循环
                        while rear.next != self.__head:
                            rear = rear.next
                        rear.next = cur.next
                        self.__head = cur.next
                        return
                    else:
                        pre.next = cur.next
                        return
                else:
                    pre = cur
                    cur = cur.next
            # 判断最后一个节点的元素
            if cur.elem == item:
                pre.next = self.__head

if __name__ == "__main__":
    li = SingleCycleLinkList()
    print(li.is_empty())    # True
    print(li.length())    # 0
    li.add("z")
    li.append(1)
    li.append(2)
    print(li.is_empty())  # False
    print(li.length())    # 3
    li.travel()    # z 1 2
    li.insert(2, "w")
    li.travel()    # z w 1 2
    li.insert(-1, 100)
    li.travel()    # 100 z w 1 2
    li.insert(5, 99)
    li.travel()  # 100 z w 1 99 2
    li.insert(7, 31)
    li.travel()  # 100 z w 1 99 2 31
    print(li.search(100))    # True
    print(li.search(99))    # True
    print(li.search(31))    # True
    print(li.search(7))    # False
    li.remove(99)
    li.travel()    # 100 z w 1 2 31
    li.remove(100)
    li.travel()    # z w 1 2 31
    li.remove(31)
    li.travel()    # z w 1 2
    li.remove(7)
    li.travel()    # z w 1 2
    li_2 = SingleCycleLinkList()
    li_2.append(127)
    li_2.travel()    # 127
    li_2.remove(127)
    li_2.travel()    # 为空
