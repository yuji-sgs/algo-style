"""
N 人が 100 点満点のテストを受けたところ、それぞれの点数は A0,A1,…,AN−1点でした。 
このテストにおける点数の中央値 A~ を求めるプログラムを作成してください。
"""

N = int(input())
A = list(map(int, input().split()))

A.sort()

if N % 2 != 0:
    print(A[N // 2])
else:
    print((A[N // 2 - 1] + A[N // 2]) / 2)
