"""
N 個の整数 A0,A1,…,AN−1と、整数 V が与えられます。
これらの整数の中から、いくつかの整数を選んで総和をとります。 
総和を V にすることが可能かどうかを判定してください。
"""

N, V = map(int, input().split())
A = list(map(int, input().split()))

sums = set()
for i in range(1 << N):
    sum = 0
    for j in range(N):
        if (i >> j) & 1:
            sum += A[j]
    sums.add(sum)

if V in sums:
    print("Yes")
else:
    print("No")
