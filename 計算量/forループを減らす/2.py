"""
N 個の整数 A0,A1,…,AN−1が与えられます。 これらの整数から 1 個選んで除外します。
残りの N−1 個の整数の総和として考えられる最大値を求めてください。
なお、答えが 32bit 整数型に収まらない可能性があることに注意してください。
"""

N = int(input())
A = list(map(int, input().split()))

min_A = min(A)
change_A = A.remove(min_A)

sum = 0

for i in range(N-1):
    sum += A[i]

print(sum)
