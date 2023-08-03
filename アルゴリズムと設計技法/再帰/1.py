# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10**6)

def rec(N):
    if N == 0:
        return 0
    else:
        return N + rec(N-1)

N = int(input())
print(rec(N))
