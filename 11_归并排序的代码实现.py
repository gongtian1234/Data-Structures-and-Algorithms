# 归并排序，先把序列逐次拆分成单个的元素，然后在比较大小，依次添加到新的列表中
# 【注意】对比快速排序，快速排序中并未生成新的列表；
#         两者的共同点是：都采用了递归的方法


def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        # return    # 【注意】返回时，你得把人家的值给人返回去，如果不返，每次都return空，那不是把列表刷空了？？？
        return alist
    # gap = n // 2
    mid = n // 2
    # left_li = alist[:gap]
    # right_li = alist[gap:]    # 【注意】因为 right_li 和 left_li 是动态变化的
    # left_li = merge_sort(left_li)
    left_li = merge_sort(alist[:mid])    # 【注意】每次递归，都把排序结果返回，所以得找一个值接收才行
    # right_li = merge_sort(right_li)
    right_li = merge_sort(alist[mid:])
    left = 0
    right = 0
    result = []
    # 以下是执行排序的代码
    while left < len(left_li) and right < len(right_li):
        # if left_li[left] < right_li[right]:
        if left_li[left] <= right_li[right]:    # 【注意】添加“等号”主要目的是为了保证算法的稳定性
            result.append(left_li[left])
            left += 1
        elif left_li[left] > right_li[right]:
            result.append(right_li[right])
            right += 1
    result += left_li[left:]
    result += right_li[right:]
    return result

if __name__ == "__main__":
    li = [123, 79, 213, 132, 45, 1, 48]
    print(li)
    sorted_li = merge_sort(li)
    print(li)
    print(sorted_li)
