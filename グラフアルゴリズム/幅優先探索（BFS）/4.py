"""
有向グラフが有向サイクルを持つかどうかを判定する問題です。
有向グラフの「ソース」 を始点として、幅優先探索に類似した「キューの使い方」で判定できることが知られています。

カメのアルルは N 個の課題に取り組んでいます。 
それぞれの課題には 0 から N−1 までの番号が振られています。 
アルルは課題に効率的に取り組むため、次のような M 個のルールを作りました (0≤i≤M-1)。
-- 課題Fiを終えるまで課題Siに取り組むことはできない。--
アルルがすべての課題を終えることができるか答えてください。
"""
from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
deg = [0] * N # 各頂点の出次数を管理する配列

for i in range(N):
    F, S = map(int, input().split())
    G[F].append(S)
    deg[S] += 1

q = deque()

num = 0
for v in range(N):
    if deg[v] == 0:
        q.append(v)
        num += 1

while len(q) > 0:
    v = q.popleft()
    
    for v2 in G[v]:
        deg[v2] -= 1

        if deg[v2] == 0:
            q.append(v2)
            num += 1

print("Yes" if num == N else "No")
