# -*- coding: UTF-8 -*-

# 冒泡排序 时间 O(n^2)
def bubble_sort(list):
    n = len(list)
    if n<2: return list
    for i in range(n-1, -1, -1):
        print('i:{}'.format(i))
        for j in range(i):
            if j+1>=n: break
            if list[j+1]<list[j]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


# 希尔排序 时间 O(nlogn)
def shell_sort(list):
    n = len(list)
    # 初始步长
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # 每个步长进行插入排序
            temp = list[i]
            print('gap:{}; temp:{}'.format(gap, temp))
            j = i
            # 插入排序
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        # 得到新的步长
        gap = gap // 2
    return list

# 归并排序
def merge_sort(li):
    #这里接收两个列表
    def merge(left, right):
        # 从两个有顺序的列表里边依次取数据比较后放入result
        # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
        result = []
        while len(left) > 0 and len(right) > 0:
            #为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        #while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
        if left: result += left
        if right: result += right
        return result

    #不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
    if len(li) == 1:
        return li

    #取拆分的中间位置
    mid = len(li) // 2
    #拆分过后左右两侧子串
    left = li[:mid]
    right = li[mid:]

    #对拆分过后的左右再拆分 一直到只有一个元素为止
    #最后一次递归时候ll和lr都会接到一个元素的列表
    # 最后一次递归之前的ll和rl会接收到排好序的子序列
    ll = merge_sort(left)
    rl = merge_sort(right)

    # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
    # 这里我们调用拎一个函数帮助我们按顺序合并ll和lr
    return merge(ll, rl)

# 快速排序
def quick_sort(arr):
    less = []
    greater = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for x in arr[1:]:
            if x < pivot:
                less.append(x)
            else:
                greater.append(x)
        return quick_sort(less) + [pivot] + quick_sort(greater)

# 堆排序
def heap_sort(list):
    # 最大堆调整
    def sift_down(lst, start, end):
        root = start
        while True:
            child = 2 * root + 1
            # 子节点为最后一个了
            if child > end:
                break
            # 左孩子小于右孩子
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            # 根节点root小于俩孩子中最大的那个child，交换root和child
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 创建最大堆
    # start代表有孩子的节点
    for start in range((len(list) - 2) // 2, -1, -1):
        print("Start:{}; Value:{}".format(start, list[start]))
        sift_down(list, start, len(list) - 1)

    # 堆排序
    for end in range(len(list) - 1, 0, -1):
        print("End:{}; Value:{}".format(end, list[start]))
        list[0], list[end] = list[end], list[0]
        sift_down(list, 0, end - 1)
    return list


unsort_list = [80, 25, 15, 0, 9, 3, 102, 22, 12, 56, 89]
# print(shell_sort(unsort_list))
print(bubble_sort(unsort_list))