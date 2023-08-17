"""
頂点数が N、辺数が M の単純有向グラフが与えられます。 
各頂点には 0,1,…,N−1 と番号が振られています。 
また、i(=0,1,…,M−1) 番目の辺は、頂点 aiから頂点 biに向かって伸びています。
このグラフの各頂点を、次のような再帰関数 rec() の手続きにしたがって探索します。
ここで G[v] は、与えられたグラフにおいて、頂点 v を始点とする各辺の終点となる頂点を、 頂点番号が小さい順に格納したものを表します。
rec(0) を呼び出したときの、出力結果を求めてください。 
なお与えられるグラフにおいては、任意の頂点 v に対して、頂点 0 から頂点 v へ到達可能であることが保証されています。
"""

def bfs(v):
    seen[v] = True
    print(v, end = " ")
    for nv in G[v]:
        if seen[nv]:
            continue
        bfs(nv)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
seen = [False] * N

for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

for v in range(N):
    G[v].sort()

bfs(0)
