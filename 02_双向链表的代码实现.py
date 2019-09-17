class Node(object):
    """单个节点"""
    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    """双向链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """从头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        cur = self.__head
        node.next = cur
        self.__head = node
        cur.prev = node

    def append(self, item):
        """从尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        node.prev = cur    # 【注意】这是双向链表，next链接好了之后，关键还要把“prev”链接好

    def insert(self, pos, item):
        """在位置前插入元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                cur = cur.next
            # cur当前指向要在其前面插入新元素的元素
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
            # cur.prev = node
            # node.prev.next = node

    def remove(self, item):
        """删除元素"""
        if self.is_empty():
            return
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:    # 【注意】当要删除的元素在头部时
                    self.__head = cur.next
                    cur.next.prev = None
                    return
                elif cur.next is None:   # 【注意】当要删除的元素在尾部时
                    cur.prev.next = None
                    return
                else:    # 【注意】当要删除的元素在中间时
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    return
            else:
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    li = DoubleLinkList()
    print(li.is_empty())    # True
    print(li.length())    # 0
    li.add("z")
    li.add(1)
    li.travel()    # 1 z
    li.append(45)
    li.append(49)
    li.travel()    # 1 z 45 49
    li.insert(2, 7)
    li.travel()    # 1 7 z 45 49
    li.insert(-1, 90)
    li.travel()   # 90 1 7 z 45 49
    li.insert(6, 47)
    li.travel()    # 90 1 7 z 45 47 49
    li.insert(8, 56)
    li.travel()    # 90 1 7 z 45 47 49 56
    li.remove(47)
    li.travel()    # 90 1 7 z 45 49 56
    li.remove(56)
    li.travel()    # 90 1 7 z 45 49
    li.remove(90)
    li.travel()    # 1 7 z 45 49
    print(li.search("z"))    # True
    print(li.search(2))    # False
    print(li.search(49))    # True
