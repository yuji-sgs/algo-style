"""
次の条件をみたす N 個の整数組 A = (a0, a1, …, aN−1) をすべて求めてください。
・ L ≤ a0 ≤ a1 ≤ … ≤ aN−1 ≤ R
"""

import sys
sys.setrecursionlimit(10**6)

N, L, R = map(int, input().split())

def func(n, l, r):
    if l > r:
        return []
    elif n == 0:
        return [[]]
    ans = []
    # n-1 番目の要素として l を選んだ場合
    for x in func(n-1,l,r):
        to = [l]
        to.extend(x)
        ans.append(to)
    # l を選ばなかった場合
    ans.extend(func(n,l+1,r))
    
    return ans

# 出力
for x in func(N,L,R):
    print(*x)
