"""
N 個の整数 A0,A1,…,AN-1が与えられます。
次の条件を満たす整数の組 (i,j) (0≤i,j≤N-1) の個数を求めてください。
Ai+ Aj≥ K が成り立つ。
"""
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

def binary_search(key):
    left = 0
    right = N

    while left < right:
        mid = (left + right) // 2
        if A[mid] >= K - key:
            right = mid
        else:
            left = mid + 1
    return left

cnt = 0
for i in range(N):
    cnt += N - binary_search(A[i])

print(cnt)
