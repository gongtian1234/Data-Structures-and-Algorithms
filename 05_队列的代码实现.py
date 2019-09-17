# 队列的特点：先进先出；同时一端操作进，另一端操作出
class Queue(object):
    """队列的代码实现"""
    def __init__(self):
        self.__head = []

    def enqueue(self, item):
        """往队列里添加元素"""
        self.__head.append(item)    # 时间复杂度为O(1)

    def dequeue(self):
        """从队列中往出取元素"""
        return self.__head.pop(0)    # 一端添加元素，一端取出元素1

    def is_empty(self):
        """判断队列是否为空"""
        # return self.__head == []
        return not self.__head

    def size(self):
        """判断队列的大小"""
        return len(self.__head)

if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())    # True
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(7)
    q.enqueue(6)
    print(q.size())    # 4
    print(q.is_empty())    # False
    print(q.dequeue())    # 1
    print(q.dequeue())    # 2
    print(q.dequeue())    # 7
    print(q.dequeue())    # 6
    print(q.size())    # 0
