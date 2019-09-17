# 选择排序法，可以选择最大或者最小进行排序；缺点是选择排序法不稳定
# 每次选择最大（小）的元素，放入指定位置，进而实现排序


def select_sort(alist):
    """选择排序法"""
    n = len(alist)
    # 1> 每次选择最大的元素
    # for j in range(0, n-1):    # 一共需要进行 n-1 次
    #     max_index = n - 1 - j    # 先假设下标为 n-1 的元素是最大的
    #     for i in range(0, n-1-j):    # 第一次比较 n-1 次，第二次比较 n-2 次，第三次比较 n-3 次
    #         if alist[max_index] < alist[i]:
    #             max_index = i
    #     alist[n-1-j], alist[max_index] = alist[max_index], alist[n-1-j]

    # 2> 每次选择最小的元素
    for j in range(0, n-1):    # 一共需要操作 n-1 次
        min_index = j    # 先假设最小值的下标为0
        for i in range(j+1, n):    # 第一次需要比较 n-1 次，第二次需要比较 n-2 次，第三次需要比较 n-3 次，
            if alist[min_index] > alist[i]:
                min_index = i
        alist[min_index], alist[j] = alist[j], alist[min_index]    # 【注意】这句话一定要放在“for i”循环的外面

if __name__ == "__main__":
    li = [123, 79, 213, 132, 45, 1, 48]
    print(li)
    select_sort(li)
    print(li)
