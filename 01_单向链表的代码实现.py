class Node(object):
    """单链表的节点"""
    def __init__(self,elem):
        # 存放数据
        self.elem = elem
        # 存放下一个节点标识
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head==None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur!=None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur!=None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():    # 【注意】判断极端情况
            self.__head = node
        else:
            cur = self.__head
            while cur.next!=None:
                cur = cur.next
            cur.next = node

    def add(self, item):
        """链表头部添加元素"""
        cur = self.__head
        node = Node(item)
        self.__head = node
        node.next = cur

    def insert(self, pos, item):
        """在指定的位置前添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            # cur = self.__head
            pre = self.__head    # 要让箭头停在要插入的位置前
            count = 1    # 【注意】count要从1开始，因为是插在目标位置前面，如果从0开始，则会多数一个位置
            while count < (pos-1):
                count += 1
                pre = pre.next
                # cur = cur.next
            node = Node(item)
            node.next = pre.next
            pre.next = node
            # node.next = cur.next
            # cur.next = node

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur!=None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        """删除节点，先输入要删除的元素"""
        if self.is_empty():
            return
        # elif cur == self.__head:
        #     self.__head = None
        else:
            cur = self.__head
            pre = None
            while cur!=None:    # 【注意】如果是 cur.next!=None ，则循环无法进如最后一个节点，进而导致无法删除
                if cur.elem == item:
                    # 删除的是头节点
                    if cur == self.__head:
                        self.__head = cur.next
                    # 删除的是中间的节点
                    else:
                        pre.next = cur.next
                    return
                else:
                    pre = cur    # 【注意】让pre指向cur当前所在的位置，然后cur再指向下一个位置
                    cur = cur.next

if __name__=="__main__":
    list = SingleLinkList()
    print(list.length())    # 0
    print(list.is_empty())    # True
    list.append(1)
    list.append(2)
    list.append(7)
    list.travel()    # 1 2 7
    list.add("z")
    list.travel()    # z 1 2 7
    list.insert(2, 3)
    list.travel()    # z 3 1 2 7
    list.insert(-2, 10)
    list.travel()    # 10 z 3 1 2 7
    print(list.search("z"))    # True
    list.remove(10)    # z 3 1 2 7
    list.remove(3)    # z 1 2 7
    list.travel()    # z 1 2 7
