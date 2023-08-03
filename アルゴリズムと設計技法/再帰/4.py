"""
フィボナッチ数列（高速化　O(N)）
"""

import sys
sys.setrecursionlimit(10**6)

N = int(input())

fib = [-1] * (N+1)
fib[0] = 0
fib[1] = 1

def func(x):
    if fib[x] != -1:
        return fib[x]
    else:
        fib[x] = func(x-1) + func(x-2)
        return fib[x] 

print(func(N))
