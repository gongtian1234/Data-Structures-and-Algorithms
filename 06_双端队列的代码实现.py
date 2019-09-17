# 双端队列：两端都可以添加或取出元素
class Deque(object):
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """从对头添加元素"""
        self.__list.insert(0, item)

    def add_wear(self, item):
        """从队尾图添加元素"""
        self.__list.append(item)

    def pop_front(self):
        """从队头取出元素"""
        return self.__list.pop(0)

    def pop_wear(self):
        """从队尾取出元素"""
        return self.__list.pop(-1)

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """判断队列的大小"""
        return len(self.__list)

if __name__ == "__main__":
    d = Deque()
    print(d.is_empty())    # True
    print(d.size())    # 0
    d.add_wear(7)
    d.add_wear(2)
    d.add_wear(1)
    d.add_front("w")
    d.add_front("z")    # z w 7 2 1
    print(d.is_empty())    # False
    print(d.size())    # 5
    print(d.pop_front())    # z
    print(d.pop_front())    # w
    print(d.pop_front())    # 7
    print(d.pop_wear())    # 1
    print(d.pop_front())   # 2
