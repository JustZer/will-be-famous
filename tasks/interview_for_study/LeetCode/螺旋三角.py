# -*- coding: utf-8 -*-
# @Time : 2022/6/16 14:17
# @Author : Zhangzixu
# @Software: PyCharm
# @Description:
n = int(input())
s = [[0 for i in range(n)] for i in range(n)]
num = 1

for i in range(n):
    # 给行赋值
    for j in range(i, n - 2 * i - 1):
        s[i][j] = num
        num += 1
    # 给对角线赋值
    for j in range(i, n - 2 * i - 1):
        s[j][n - i - j - 1] = num
        num += 1
    # 给列赋值
    for j in range(i, n - 2 * i - 1):
        s[n - i - j - 1][i] = num
        num += 1

if (n - 1) % 3 == 0:
    # 有的数最中间会只有一个数而不是一个圈，所以不在赋值范围内故需要特殊照顾
    s[(n - 1) // 3][(n - 1) // 3] = num

for i in range(n):
    for j in range(n):
        if s[i][j] != 0:
            print('{:>4d}'.format(s[i][j]), end='')
    print()
