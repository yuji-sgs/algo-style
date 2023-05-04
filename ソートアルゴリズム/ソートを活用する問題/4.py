"""
N 個の整数 A0,A1,…,AN−1が与えられます。
この中から K 個の整数を「最大値と最小値の差」ができるだけ小さくなるよう選んだとき、 K 個の整数の「最大値と最小値の差」はいくつになりますか。
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

min_diff = float('inf') # 変数を無限大の値で初期化

for i in range(N - K + 1):
    diff = A[i + K - 1] - A[i]
    min_diff = min(min_diff, diff) # 最小値を更新

result = min_diff
print(result)
