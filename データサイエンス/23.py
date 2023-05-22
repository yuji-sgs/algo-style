"""
N 要素の 2 つのデータ A=(A0,A1,…,AN−1) と B=(B0,B1,…,BN−1) が与えられます。
データ A,B の相関係数 r を求めたとき、
r>0.3 であれば、正の相関がある
r<−0.3 であれば、負の相関がある
そのどちらでもなければ、相関がない
と、ここでは呼ぶことにします。 A と B の間に、正/負の相関があるか、または相関がないかを答えてください。
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

# 判定
if corr > 0.3:
    print("Positive")
elif corr < -0.3:
    print("Negative")
else:
    print("No correlation")
