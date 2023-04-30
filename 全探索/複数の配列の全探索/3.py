"""
X個の整数 A0,A1,…,AX−1と、Y個の整数B0,B1,…,BY−1と、Z個の整数C0,C1,…,CZ−1が与えられます。
次の条件を満たす組 (i,j,k) の個数を答えるプログラムを作成してください。
・i は 0 以上 X−1 以下の整数
・j は 0 以上 Y−1 以下の整数
・k は 0 以上 Z−1 以下の整数
・Ai + Bj = Ck
"""

x, y, z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

count = 0

for i in range(x):
    for j in range(y):
        for k in range(z):
            if A[i] + B[j] == C[k]:
                count += 1

print(count)
