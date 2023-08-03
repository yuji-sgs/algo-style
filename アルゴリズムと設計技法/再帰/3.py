"""
フィボナッチ数列
"""

import sys
sys.setrecursionlimit(10 ** 6)

def fib(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fib(N-1) + fib(N-2)

N = int(input())
print(fib(N))
