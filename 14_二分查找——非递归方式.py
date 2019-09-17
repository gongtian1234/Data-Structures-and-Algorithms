# 二分查找：非递归的方式，此时则采用while循环让整个程序内部自己动起来
def binary_search(alist, item):
    """非递归方式的二分查找"""
    n = len(alist)
    # mid = n // 2
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            last = mid - 1
        elif item > alist[mid]:
            first = mid + 1
    return False

if __name__ == "__main__":
    li = [1, 45, 48, 79, 123, 132, 213]
    print(li)
    print(binary_search(li, 123))    # True
    print(binary_search(li, 12))    # False
    print(binary_search(li, 1))    # True
    print(binary_search(li, 1289))    # False
    print(binary_search(li, 48))    # True
    # li_2 = []
    # print(binary_search(li_2, 48))    # False
