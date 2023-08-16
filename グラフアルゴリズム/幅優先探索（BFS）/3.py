"""
カメのアルルは縦 H マス横 W マスのゲーム盤と 1 つのコマを持っています。
ゲーム盤の状態は H 個の長さ W の文字列で管理されており、 ゲーム盤の上から i マス目、 左から j マス目をマス (i,j) と表すこととすると、 マス (i,j) の状態は S i,jが管理しています。 
Si,j= B のときマス (i,j) は黒く塗られており、 Si,j= W のときはマス (i,j) は白く塗られています。
アルルは、このゲーム盤のマス (X0,Y0) の上にコマを置き、次のルールに従いながらコマをマス (X1,Y1) まで動かします。
・上下左右にとなりあっているマスのうちいずれかに移動する。
・ただし、黒く塗られているマスには移動することができない。
コマがマス (X1,Y1) にたどりつくためには少なくとも何回動かす必要があるか答えてください。 
ただし、コマがゴールにたどり着けることと、マス (X0,Y0) とマス (X1,Y1) は白く塗られていることが保証されています。
"""
from collections import deque

H, W = map(int, input().split())
sy, sx, gy, gx = map(int, input().split())

# 迷路の入力
grid = [input() for _ in range(H)]

# 最初にスタート地点をキューに入れる
q = deque()
q.append((sy, sx))

# スタートから各マスまでの最短距離を管理する2次元配列
INF = 10 ** 9
dist = [[INF for _ in range(W)] for _ in range(H)]
dist[sy][sx] = 0

# 4方向への移動ベクトル
dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

# 幅優先探索
while len(q) > 0: # キューが空になるまで繰り返す
    
    # キューの先頭を取り出す
    now = q.popleft()
    
    # 取り出したキューのy, x座標を定義
    y, x = now
    
    # 隣接する4マスを探索
    for di in range(4):
        
        # 移動した後の点を (ny, nx) とする
        ny = y + dy[di]
        nx = x + dx[di]
        
        # 移動が可能かの判定と既に訪れたことがあるかの判定
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if grid[ny][nx] == "B":
            continue
        if dist[ny][nx] != INF:
            continue
        
        # 移動できるならキューに入れ、その点の距離を更新
        dist[ny][nx] = dist[y][x] + 1
        q.append((ny, nx))
        
print(dist[gy][gx])
