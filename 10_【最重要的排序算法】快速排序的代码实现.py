# 快速排序算法：有两个游标，而且此时是【注意】【错误思路：生成不同的序列进行处理，之后再拼接】针对同一列表，并未生成新的
# 是根据中间值将大于中间值的元素移到其右，小于中间值的元素移到其左
# 【注意】归并排序才是生成新的列表，快速排序自始至终都是针对一个序列，并无新序列生成


def quick_sort(alist, first, last):
    """快速排序"""
    if first == last:
        return
    left_cur = first
    right_cur = last
    # mid_value = alist[0]    # 【注意】如果每次都是用这个条件，则会使程序陷入无限循环中
    mid_value = alist[first]
    while left_cur < right_cur:    # 主要是为了避免两个游标错过
        while left_cur < right_cur and alist[right_cur] >= mid_value:
            right_cur -= 1    # 【注意】目的是让我右边的游标往左走
        alist[left_cur], alist[right_cur] = alist[right_cur], alist[left_cur]
        while left_cur < right_cur and alist[left_cur] < mid_value:
            left_cur += 1
        alist[left_cur], alist[right_cur] = alist[right_cur], alist[left_cur]
    alist[left_cur] = mid_value    # 此时左右游标的值是相同的
    # 上述过程只是完成了第一次循环
    if (len(alist[:left_cur])-1) >= 0:
        # quick_sort(alist[:left_cur], 0, len(alist[:left_cur])-1)
        quick_sort(alist, 0, left_cur-1)    # 【注意】作用在同一列表上，上面那种方法会生成新列表
    else:
        return
    if (len(alist[left_cur+1:])-1) >= 0:
        # quick_sort(alist[left_cur+1:], 0, len(alist[left_cur+1:])-1)
        quick_sort(alist, left_cur+1, len(alist)-1)    # 【注意】作用在同一列表上，上面那种方法会生成新列表
    else:
        return

if __name__ == "__main__":
    li = [123, 79, 213, 132, 45, 1, 48]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)
