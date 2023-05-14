"""
N 個の要素からなる 2 つのデータ A,B があり、平均値はともに 0 です。 
A と B のどちらの分散が小さいかを求めるプログラムを作成してください。
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 初期値を設定
A_scatter = 0
B_scatter = 0

for i in range(N):
    A_scatter += A[i] ** 2
    B_scatter += B[i] ** 2

A_scatter = A_scatter / N
B_scatter = B_scatter / N

if A_scatter < B_scatter:
    print("A")
elif B_scatter < A_scatter:
    print("B")
else:
    print("same")
