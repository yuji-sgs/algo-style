"""
N 個の整数からなる数列 A0,A1,…,AN−1が与えられます。
この数列に対して、以下の Q 回の質問に答えてください。
各質問では整数値 k (0≤k≤N) が与えられます。
A0+A1+⋯+Ak−1の値を求めてください。
つまり、数列の左端から k 個分の値の総和を求めてください。
"""

# 入力
N = int(input())
A = list(map(int, input().split()))

# 累積和を求める
# acc[k]: 左から k 個分の総和
acc = [0] * (N+1)
for idx, a in enumerate(A):
    acc[idx+1] = acc[idx] + a

# 質問に答える
Q = int(input())
for _ in range(Q):
    k = int(input())
    print(acc[k])
