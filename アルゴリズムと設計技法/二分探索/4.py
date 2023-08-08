"""
N 個の整数 A0,A1,…,AN-1と、M 個の整数 B0,B1,…,BM-1が与えられます。
k=0,1,…,M-1 について次の問いに答えてください。
Ax≤ Bkを満たすx の個数を求めよ。
"""
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()

def binary_search(key):
    left = 0
    right = N

    while left < right:
        mid = (left + right) // 2
        if A[mid] <= key:
            left = mid + 1
        else:
            right = mid
    return left

for b in B:
    cnt = binary_search(b)
    print(cnt)
