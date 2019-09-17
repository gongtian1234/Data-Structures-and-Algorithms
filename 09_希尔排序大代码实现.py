# 希尔排序，插入排序的改进版本，增加了gap


def shell_sort(alist):
    """希尔排序算法"""
    n = len(alist)
    # 特殊情况，只有一个数
    if n <= 1:
        return
    gap = n // 2    # n//2 是对结果取整数部分
    while gap >= 1:    # gap变化到0之前，插入算法的执行次数
        # 以下是插入算法，与普通插入算法的区别就是gap步长
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break    # 对程序的优化
        gap //= 2

if __name__ == "__main__":
    li = [123, 79, 213, 132, 45, 1, 48]
    print(li)
    shell_sort(li)
    print(li)
