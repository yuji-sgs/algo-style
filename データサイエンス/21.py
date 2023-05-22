"""
あるクラスには 0 から N−1 までの番号が振られた N 人の生徒がいます。
N 人が数学と英語のテストを受けたところ、生徒 i の数学と英語の点数はそれぞれ Ai,Bi[点] でした。 (0≤i≤N−1)
このデータにおける A,B の共分散 σABを求めてください。
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mean_A = sum(A) / N
mean_B = sum(B) / N

ans = 0

for i in range(N):
    ans += (A[i] - mean_A) * (B[i] - mean_B)

ans = ans / N

print(ans)
