# 冒泡算法是一种排序算法，且这种算法是稳定的
# 【注意】第一次程序有bug，当运行至某一步序列阴差阳错的排好时，程序还会往下执行


def bubble_sort(alist):
    """冒泡排序算法"""
    n = len(li)
    for j in range(0, n-1):    # 总共需要走 n-1 次
        count = 0
        for i in range(0, n-1-j):    # 第一次游标i需要走 n-1 次(此时 j=0),第二次游标i需要走 n-2 次( j=1 )【先创建内层循环，再外层循环】
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            break
            # return

if __name__ == "__main__":
    li = [123, 152, 213, 132, 45, 1, 48]
    print(li)
    bubble_sort(li)
    print(li)
