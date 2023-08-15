"""
カメのアルルの通う学校には N 人の生徒がいます。 
それぞれの生徒には 0 から N-1 までの番号が割り振られており、アルルの番号は 0 です。 
N 人の交友関係は次の M 個であることがわかっています。
生徒Aiと生徒Biは友達同士である (0 ≤ i ≤ M-1)

アルルはスモール・ワールド現象というものを知り、 いくつの交友関係をたどれば全ての生徒に会えるかが気になりました。
アルルの代わりに次の問いに答えてください。
アルル (生徒0) が交友関係をたどっていったときに、友達i に最短経路で会うまでのたどる回数をdiとします(1 ≤ i ≤ N−1)。
max(d1, d2, ⋯, dN−1) の値を答えてください。
ただし、どの生徒間も友達関係をたどることで会うことが保証されています。
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

while len(q) > 0:
    v = q.popleft()

    for next_v in G[v]:
        if dist[next_v] != -1:
            continue

        dist[next_v] = dist[v] + 1
        q.append(next_v)

print(max(dist))
