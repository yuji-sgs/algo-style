"""
部分和問題（再帰）
N 個の整数 A0, A1, …, AN−1の中から総和が X と等しくなるようにいくつかの数字を選べますか。
"""

import sys
sys.setrecursionlimit(10**6)

N, X = map(int, input().split())
A = list(map(int, input().split()))

def func(i, j):
    if i == 0:
        if j == 0:
            return True
        else:
            return False
    else:
        if j >= A[i-1] and func(i-1, j-A[i-1]):
            return True
        elif func(i-1, j):
            return True
        else:
            return False

print("Yes") if func(N, X) else print("No")
