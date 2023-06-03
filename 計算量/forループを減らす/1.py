"""
N 個の整数A0,A1,…,AN−1が与えられます。
これらの整数から 2 個選びます (重複してもよいです)。 選んだ 2 個の整数の差の最大値を求めてください。
"""

N = int(input())
A = list(map(int, input().split()))
ans = max(A) - min(A)
print(ans)
