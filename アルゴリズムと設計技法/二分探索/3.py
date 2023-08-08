"""
N 個の整数 A0,A1,…,AN-1と、M 個の整数 B0,B1,…,BM-1が与えられます。
A0,A1,…,AN-1はすべて異なり、小さい順に並んでいます。
つまり、 A0<A1<⋯<AN-1が成り立ちます。
k=0,1,…,M-1 について次の問いに答えてください。
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def birary_search(key):
    left = 0
    right = N-1

    while left != right:
        mid = (left + right) // 2

        if A[mid] >= key:
            right = mid
        else:
            left = mid + 1

    return left

for i in range(M):
    print(birary_search(B[i]))
