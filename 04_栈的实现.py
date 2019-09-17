# 栈的特点：后进先出；同时也只在一端进行进出操作
class Stack(object):
    """栈的代码实现"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """压栈：添加一个新的元素item到栈顶"""
        self.__list.append(item)    # 在列表尾部添加元素，时间复杂度为O(1)

    def pop(self):
        """出栈：弹出栈顶元素"""
        return self.__list.pop(-1)

    def peek(self):
        """返回栈顶元素，但不让这个元素出栈"""
        # 【注意】返回栈顶元素的代码为：self.__list[-1]
        if self.__list == []:    # 特殊情况，空栈
            return None
        else:
            return self.__list[-1]

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []
        # return not self.__list

    def size(self):
        """判断栈的大小"""
        return len(self.__list)

if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())    # True
    s.push(1)
    s.push(2)
    s.push(7)
    print(s.peek())    # 7
    print(s.size())   # 3
    print(s.pop())   # 7
    print(s.pop())    # 2
    print(s.peek())    # 1
    print(s.pop())    # 1
    print(s.size())    # 0
    print(s.peek())    # None
