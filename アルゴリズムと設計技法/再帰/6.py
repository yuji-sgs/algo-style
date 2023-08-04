"""
部分和問題（再帰 - メモ化）
N 個の整数 A0, A1, …, AN−1の中から総和が X と等しくなるようにいくつかの数字を選べますか。
"""

import sys
sys.setrecursionlimit(10**6)

N, X = map(int, input().split())
A = list(map(int, input().split()))

memo = {}

def func(i, j):
    if (i, j) in memo:
        return memo[(i, j)]
    else:
        if i == 0:
            if j == 0:
                result = True
            else:
                result = False
        else:
            if j >= A[i-1] and func(i-1, j-A[i-1]):
                result = True
            elif func(i-1, j):
                result = True
            else:
                result = False
        memo[(i, j)] = result
        return result

print("Yes") if func(N, X) else print("No")
