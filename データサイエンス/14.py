"""
N 人が身長を測ったところ、それぞれの身長は H0,H1,…,HN−1[cm]でした。 あなたはデータの特徴をわかりやすくするために、このデータを標準化することにしました。
標準化したデータを求めるプログラムを作成してください。
"""
N = int(input())
H = list(map(int, input().split()))
mean_H = sum(H) / N  # 平均
sigma_H = (sum((i - mean_H) ** 2 for i in H) / N) ** 0.5  # 標準偏差
standard = [] * N  # 標準化のデータを入れる配列

for i in range(N):
    standard.append((H[i] - mean_H) / sigma_H)  # 標準化の計算

print(*standard)
