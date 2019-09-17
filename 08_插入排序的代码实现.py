# 插入排序是从后面无序序列中拿出第一个与有序序列一次比较，进而确定该元素的位置


def insert_sort(alist):
    """插入排序算法"""
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break    # 对程序的优化，只要第一次出现不用交换次序的情况，则表明顺序现在已排好，跳出本次循环

if __name__ == "__main__":
    li = [123, 79, 213, 132, 45, 1, 48]
    print(li)
    insert_sort(li)
    print(li)
