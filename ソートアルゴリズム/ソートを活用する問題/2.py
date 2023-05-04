"""
N 個の異なる整数 A0,A1,…,AN−1が与えられます。
N 個の整数のうち、 Xk 番目に小さい数はいくつですか。（k=0,1,…,M−1）
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))

# ソート
A.sort()

for i in range(len(X)):
    print(A[X[i]])
