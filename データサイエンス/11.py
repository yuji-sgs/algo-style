"""
N 人が身長を測ったところ、それぞれの身長は H0,H1,…,HN−1[cm]でした。 
あなたはデータの特徴をわかりやすくするために、各要素を K 倍する補正をかけることにしました。
補正前と補正後のデータの分散をそれぞれ σH,σXとおくとき、σX^2が σH^2の何倍か求めるプログラムを作成してください。
"""

N, K = map(int, input().split())
H = list(map(int, input().split()))
comp = [] * N  # 補正後のデータを入れる配列

for i in range(N):
    comp.append(H[i] * K)

mean_H = sum(H) / N  # 補正前データの平均
mean_comp = sum(comp) / N  # 補正後データの平均 

sigma_H = sum((i - mean_H) ** 2 for i in H) / N  # 補正前データの分散
sigma_comp = sum((i - mean_comp) ** 2 for i in comp) / N  # 補正後データの分散

print(sigma_comp / sigma_H)
