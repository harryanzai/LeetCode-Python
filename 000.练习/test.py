# -*- coding: UTF-8 -*-
def pow(x, n):
    pow = 1
    while n:
        print('n当前的值：{}'.format(n))
        # 奇数
        if n & 1:
            pow *= x
        x *= x
        n >>= 1
    return pow


# print(pow(int(input('X：')), int(input('n：'))))
import re


# str = '  ￥%6767xffgdgf fgfd'
# str = re.findall('^[\+\-]?\d+', str.lstrip())
# print(int(*str))
#
#
# def is_palindrome(num):
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp //= 10
#         print(temp, total)
#     return total == num
#
#
# print(is_palindrome(1234321))
#
#
# def dfs(root):
#     def _dfs(node, level):
#         if not node: return
#         if len(result) < level + 1:
#             result.append([])
#         result[level].append(node.val)
#         _dfs(node.left, level + 1)
#         _dfs(node.right, level + 1)
#
#     if not root: return []
#     result = []
#     _dfs(root, 0)
#     return result
def mySqrt(x):
    r = 100
    round = 0
    while r * r > x:
        r = (r + x / r) / 2
        round += 1
    print(round)
    return r

import  json
def test():
    root = {}
    node = root
    for i in 'abcdef':
        node = node.setdefault(i, {})

        # if not node: break
        # for k,j in node.iteritems():
        #     print(k,j)

    print(json.dumps(root))

# my_set = [1,2,3]
def testFunc(x,y):
    print("X:{}; Y:{}".format(x,y))
    return x*y

from collections import OrderedDict
cacheDict = OrderedDict()
cacheDict[2] = 123
cacheDict[3] = 234
cacheDict[1] = 111111

# cacheDict.move_to_end(3)
# for k,v in cacheDict.items():
#     print(k, v)
# mylist = [2,3,4,5,6]
# if not 2 in mylist:
#     print('Yes')
# else:
#     print('Nope')
def power(a, n):
    if n==0:
        return 1
    result, tmp = 1, a
    while n:
        print('N:', n)
        if n&1:
            result *= tmp
        n >>= 1
        tmp *= tmp
    return result

print(power(3, 7))
