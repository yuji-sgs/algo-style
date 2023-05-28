"""
縦のサイズが H、横のサイズが W のマス目に区切られた盤面があります。 各マス目は白色か黒色のいずれかに塗られています。
その入力データは、文字を H×W の長方形形状に並べたものとして与えられます。 文字 . は対応するマスが白色であることを表し、 文字 # は対応するマスが黒色であることを表します
この盤面において、Q 回のクエリが与えられました。 それぞれのクエリに答えてください。 各クエリは、次のいずれかです。
・　Push(p,q)：マス (p,q) および、その上下左右に隣接するマス (盤外を除く) の白色と黒色を反転させます
・　Get(p,q)：マス (p,q) および、その上下左右に隣接するマス (盤外を除く) の黒色マスの個数を答えてください
なお、上から p 行目 (0 始まり)、左から q 列目 (0 始まり) のマスを (p,q) と表すことにします。
"""
H, W = map(int, input().split())
table = [list(input()) for _ in range(H)]
Q = int(input())

def toggle_color(color):
    return "." if color == "#" else "#"

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        p, q = query[1], query[2]
        table[p][q] = toggle_color(table[p][q])
        if p-1 >= 0:
            table[p-1][q] = toggle_color(table[p-1][q])
        if p+1 < H:
            table[p+1][q] = toggle_color(table[p+1][q])
        if q-1 >= 0:
            table[p][q-1] = toggle_color(table[p][q-1])
        if q+1 < W:
            table[p][q+1] = toggle_color(table[p][q+1])
    elif query[0] == 1:
        p, q = query[1], query[2]
        cnt = 0
        if table[p][q] == "#":
            cnt += 1
        if p-1 >= 0 and table[p-1][q] == "#":
            cnt += 1
        if p+1 < H and table[p+1][q] == "#":
            cnt += 1
        if q-1 >= 0 and table[p][q-1] == "#":
            cnt += 1
        if q+1 < W and table[p][q+1] == "#":
            cnt += 1
        print(cnt)
