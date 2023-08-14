"""
カメのアルルは N 個の頂点と M 本の辺からなるグラフを用いて勉強をしています。 
すべての頂点には色を塗ることができ、はじめは色が塗られていません。 
また、 i 番目の辺は頂点 Aiと頂点 Biをつないでいます (0≤i≤M-1)。
アルルは次の操作を k=0,1,…,N-1 について順に行いました。
ただし、k=i のときの操作を i 回目と呼ぶことにします。
1. k=0 ならば、頂点 0 に色を塗る。
2. k≠0 ならば、 i-1 回目の操作で色が塗られた頂点と繋がっており、まだ色が塗られていない頂点に色を塗る。

k=0,1,⋯,N-1 について次の問いに答えてください。
「操作 k によって色が塗られた頂点を番号が小さい順にすべて出力せよ。」
"""
from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

q = deque()
q.append(0)

dist = [-1] * N
dist[0] = 0

# k 手目に探索された頂点集合を格納
nodes = [[] for _ in range(N)]
nodes[0].append(0)

while len(q) > 0:
    now = q.popleft()

    for next_v in G[now]:
        if dist[next_v] != -1:
            continue
        
        dist[next_v] = dist[now] + 1
        
        q.append(next_v)
        nodes[dist[next_v]].append(next_v)

for k in range(N):
    print(*sorted(nodes[k]))
