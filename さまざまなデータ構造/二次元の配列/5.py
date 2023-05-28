"""
縦のサイズが H、横のサイズが W のマス目に区切られた盤面があります。 各マスは「空き」マスか「爆弾」マスのいずれかとなっています。
この盤面について、Q 回のクエリが与えられます。 各クエリではマス (x,y) が与えられますので、そのマスの上下左右に隣接するマスのうち、 「爆弾」マスが何個あるかを答えてください。 各クエリで指定されるマス (x,y) は「空き」マスであることが保証されます。
なお、上から x 行目 (0 始まり)、左から y 列目 (0 始まり) のマスを (x,y) と表すこととします。
"""

H, W = map(int, input().split())
table = [input() for _ in range(H)]
Q = int(input())

for _ in range(Q):
    x, y = map(int, input().split())
    cnt = 0
    if x-1 >= 0 and table[x-1][y] == "#":
        cnt += 1
    if x+1 < H and table[x+1][y] == "#":
        cnt += 1
    if y+1 < W and table[x][y+1] == "#":
        cnt += 1
    if y-1 >= 0 and table[x][y-1] == "#":
        cnt += 1
    print(cnt)
