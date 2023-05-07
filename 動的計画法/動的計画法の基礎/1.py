"""
N 個の数字 A0,A1,…,AN−1が横1列に書かれています。
それぞれの数は以下のような規則を満たすことがわかっています。
A0の値はXである。
A1の値はYである。
以降の値は、前2つの数字を足して100で割った余りと等しい。   
AN−1の値を求めるプログラムを作成してください。
"""

N, X, Y = map(int, input().split())
A = []
A.append(X)
A.append(Y)

for i in range(2, N):
    A.append((A[i-2] + A[i-1]) % 100)

print(A[-1])
