"""
頂点数が N、辺数が M の単純有向グラフが与えられます。 
各頂点には 0,1,…,N-1 と番号が振られています。 
また、i(=0,1,…,M−1) 番目の辺は、頂点 aiから頂点 biに向かって伸びています。
このグラフにおいて、頂点 0 から有向辺をたどって辿り着くことが不可能な頂点の個数を求めてください。
たとえば下図のグラフにおいては、頂点 5,6 には頂点 0 から到達することはできません。
"""
def bfs(v):
    seen[v] = True
    reachable.append(v)
    for nv in G[v]:
        if seen[nv]:
            continue
        bfs(nv)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

seen = [False] * N
reachable = []
bfs(0)

print(N - len(reachable))
