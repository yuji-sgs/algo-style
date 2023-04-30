"""
N 個の整数 A0,A1,…,AN−1とM個の整数B0,B1,…,BM−1が与えられます。
次の条件を満たす組 (i,j) の個数を答えるプログラムを作成してください。

・i は 0 以上 N−1 以下の整数
・j は 0 以上 M−1 以下の整数
・Ai >Bj
"""

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(m):
        if A[i] > B[j]:
            count += 1

print(count)
