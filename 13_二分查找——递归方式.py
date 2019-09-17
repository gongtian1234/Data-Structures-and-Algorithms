# 二分查找：先以递归的方式；【注意】只能用于已经排好序的序列
def binary_search(alist, item):
    """递归方式二分查找"""
    n = len(alist)
    if n < 1:    # 特殊情况：空列表
        return False
    mid = n // 2
    if alist[mid] == item:
        return True
    elif item > alist[mid]:
        # binary_search(alist[mid+1:], item)
        return binary_search(alist[mid+1:], item)
    elif item < alist[mid]:
        # binary_search(alist[:mid], item)
        return binary_search(alist[:mid], item)
    else:
        return False

if __name__ == "__main__":
    li = [1, 45, 48, 79, 123, 132, 213]
    print(li)
    print(binary_search(li, 123))    # True
    print(binary_search(li, 12))    # False
    print(binary_search(li, 1))    # True
    print(binary_search(li, 1289))    # False
    print(binary_search(li, 48))    # True
