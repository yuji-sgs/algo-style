"""
縦のサイズが H、横のサイズが W のマス目に区切られたグリッドがあります。
グリッドの各マスは白色か黒色のいずれかに塗られています。
このグリッドにおいて、「黒色のマスの塊」が何個あるかを答えてください。 
なお、黒色のマスの塊とは、上下左右に隣接した黒色のマスの集合のことを指すものとします。
たとえば上図のグリッドの「黒色のマスの塊」の個数は 3 個です。 
左上の塊と右下の塊は点で接していますが、上下左右には隣接していませんので、別の塊とみなします。
"""

def dfs(sy, sx):
    if seen[sy][sx]:  
        return
    seen[sy][sx] = True  
    for di in range(4):
        ny = sy + dy[di]
        nx = sx + dx[di]
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if S[ny][nx] == ".":
            continue
        if not seen[ny][nx] and S[ny][nx] == "#":
            dfs(ny, nx)

H, W = map(int, input().split())
S = [input() for _ in range(H)]

dy = (0, -1, 0, 1)
dx = (1, 0, -1, 0)

seen = [[False] * W for _ in range(H)]
count = 0

for i in range(H):
    for j in range(W):
        if not seen[i][j] and S[i][j] == "#":
            dfs(i, j)
            count += 1 

print(count)
