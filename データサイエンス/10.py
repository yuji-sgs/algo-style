"""
N 人が身長を測ったところ、それぞれの身長は H0,H1,…,HN−1[cm]でした。
あなたはデータの特徴をわかりやすくするために、各要素を K 倍する補正をかけることにしました。
補正をかけたあとのデータを求めるプログラムを作成してください。
"""

N, K = map(int, input().split())
H = list(map(int, input().split()))
comp = [] * N  # 補正後のデータを入れる配列

for i in range(N):
    comp.append(H[i] * K)

print(*comp)
