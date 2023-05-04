"""
N 個の整数 A0,A1,…,AN−1が与えられます。これらの中央値A~を求めてください。
"""

# 入力
N = int(input())
A = list(map(int, input().split()))

# ソート
A.sort()

# N の偶奇に応じて出力
if N % 2 == 1:
    print(A[N // 2]) 
else:
    print((A[N // 2 - 1] + A[N // 2]) / 2)
