"""
アルル はN 本のひもを持っています。
ひもには 0 から N-1 までの番号がついており、ひも i の長さは Liです。
アルルは、これらのひもを切って同じ長さのひもを K 本用意しようと考えています。
アルルが用意できるひもの長さの最大値を求めてください。
ただし、ひも同士を連結させることはできません。
"""

def func(x,L):
    ans = 0
    for l in L:
        ans += int(l/x)        
    return ans

def binary_search(key):
    left = 0
    right = 10 ** 5

    while right - left > 1e-8:
        mid = (left + right) / 2
        if func(mid, L) >= key:
            left = mid
        else:
            right = mid

    return left

N, K = map(int, input().split())
L = list(map(int, input().split()))

print(binary_search(K))
