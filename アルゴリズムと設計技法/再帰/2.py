"""
A から B までの整数の総和を求めてください。
"""

import sys
sys.setrecursionlimit(10**6)

def rec(N):
    if N == 0:
        return 0
    else:
        return N + rec(N-1)

A, B = map(int, input().split())
print(rec(B) - rec(A-1))
