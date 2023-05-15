"""
N 人がテストを受けたところ、それぞれの点数は A0,A1,…,AN−1点でした。 
あなたはこのデータを扱いやすくするために、平均点が 0 点となるように補正をかけることにしました。(参考: 平均値をずらす)
補正前と補正後のデータの分散をそれぞれ σA^2,σB^2とおくとき、σ^B2が σ^A2の何倍か求めるブログラムを作成してください。
"""

N = int(input())
A = list(map(int, input().split()))
mean = sum(A) / N  # 平均
B = [] * N

for i in range(N):
    B.append(A[i] - mean) # 平均点が0になるように補正

sigma_A = sum((i - mean) ** 2 for i in A) / N  # Aの分散
sigma_B = sum((i - 0) ** 2 for i in B) / N  # Bの分散

print(sigma_B / sigma_A)
