"""
一般的に、人口密度の高い都心部では比較的若い世代が密集するため平均年齢が低くなり、人口密度の低い地域では平均年齢が高くなる傾向があることが知られています。
あなたはこの事実を確かめるために「2021 年度における 47 都道府県の面積, 人口, 平均年齢のデータ」を収集しました。 
それぞれの都道府県には 0 から 46 までの番号が振られており、番号 i の都道府県の名前, 面積, 人口, 平均年齢はそれぞれ Xi,S,pi,aiでした。 (0≤i≤46)
このデータを用いて、都道府県の「人口密度 [千人/㎢]」と「平均年齢 [歳]」の相関係数を求めてください。
"""

# 入力
N = 47
data = [input().split() for _ in range(N)]
X = [d[0] for d in data]
S = [float(d[1]) for d in data]
p = [float(d[2]) for d in data]
a = [float(d[3]) for d in data]

# 人口密度
density = [p[i] / S[i] for i in range(N)]

# 平均の計算
mean_density = sum(density) / N
mean_a = sum(a) / N

# 標準偏差の計算
sigma_density = (sum((i - mean_density) ** 2 for i in density) / N) ** 0.5
sigma_a = (sum((i - mean_a) ** 2 for i in a) / N) ** 0.5

# 共分散の計算
cov = 0
for i in range(N):
    cov += (density[i] - mean_density) * (a[i] - mean_a)
cov = cov / N

# 相関係数の計算
corr = cov / (sigma_density * sigma_a)
print(corr)
