"""
N 個の整数からなる数列 A0,A1,…,AN−1が与えられます。
また、0 以上 N 未満の整数からなる集合 S を表す、0 以上 2^N未満の整数からなる整数値 X が与えられます。
数列 A の項のうち、集合 S の要素を添字にもつ項の総和を求めてください。
"""

N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for i in range(N):
    if X >> i & 1: # Xをiビット右にシフトして, 1だった場合
        ans += A[i] # i番目のAの値を足す

print(ans)
