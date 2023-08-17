"""
頂点数が N、辺数が M の単純無向グラフが与えられます。 
各頂点には 0,1,…,N−1 と番号が振られています。 
また、i(=0,1,…,M−1) 番目の辺は、頂点 aiと頂点 biを結んでいます。
このグラフが連結であるかどうかを判定してください。
"""

def bfs(v):
    seen[v] = True
    for nv in G[v]:
        if seen[nv]:
            continue
        bfs(nv)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

seen = [False] * N
linking = 0 #　連結成分

for v in range(N):
    if seen[v]:
        continue
    bfs(v)
    linking += 1

print("Yes") if linking == 1 else print("No")
