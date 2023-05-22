"""

あるクラスには 0 から N−1 までの番号が振られた N 人の生徒がいます。 
N 人が数学と英語のテストを受けたところ、生徒 i の数学と英語の点数はそれぞれ Ai,Bi[点] でした。 (0≤i≤N−1)
このデータにおける A,B の相関係数 r を求めてください。
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 平均の計算
mean_A = sum(A) / N
mean_B = sum(B) / N

# 標準偏差の計算
sigma_A = (sum((i - mean_A) ** 2 for i in A) / N) ** 0.5
sigma_B = (sum((i - mean_B) ** 2 for i in B) / N) ** 0.5

# 共分散の計算
cov = 0
for i in range(N):
    cov += (A[i] - mean_A) * (B[i] - mean_B)
cov = cov / N

# 相関係数の計算
corr = cov / (sigma_A * sigma_B)

print(corr)
