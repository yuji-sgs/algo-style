"""
N 個の整数 A0,A1,…,AN−1が与えられます。
この中から K 個の整数を、できるだけ総和が大きくなるよう選んだとき、 K 個の整数の総和はいくつになりますか。
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
point = -1

A.sort()

for i in range(K):
    cnt += A[point]
    point -= 1

print(cnt)
