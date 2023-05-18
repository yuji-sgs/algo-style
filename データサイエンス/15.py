"""
N 人が身長を測ったところ、それぞれの身長は H0,H1,…,HN−1[cm]でした。 あなたはデータの特徴をわかりやすくするために、このデータを正規化することにしました。
正規化したデータを求めるプログラムを作成してください。
"""

N = int(input())
H = list(map(int, input().split()))
max_H = max(H)  # 最大値 
min_H = min(H)  # 最小値 
normal = [] * N  # 正規化後のデータを入れる配列

for i in range(N):
    normal.append((H[i] - min_H) / (max_H - min_H)) # 正規化の計算

print(*normal)
