"""
N個の整数 A0,A1,…,AN−1と整数Kが与えられます。
これらの N 個の整数から、和が K 以下となるように 2 つの数を選ぶ方法は何通りあるか求めるプログラムを作成してください。
ただし選んだ 2 つの整数の添字 (Aiの i) が等しくなってはいけないものとします。
"""

n, k = map(int, input().split())
A = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i+1,n):
        if A[i] + A[j] <= k:
            count += 1
print(count)
