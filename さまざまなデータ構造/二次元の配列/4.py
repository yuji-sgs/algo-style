"""
縦のサイズが H、横のサイズが W のマス目に区切られたグリッドがあります。 各マス目は白色か黒色のいずれかに塗られています。
その入力データは、文字を H×W の長方形形状に並べたものとして与えられます。 文字 . は対応するマスが白色であることを表し、 文字 # は対応するマスが黒色であることを表します。
このグリッドにおいて、マス (p,q) が指定されたときに、 そのマスの上下左右全体に何個の黒色マスがあるかを答えてください。
なお、上から p 行目 (0 始まり)、左から q 列目 (0 始まり) のマスを (p,q) と表すことにします。
"""

H, W = map(int, input().split())
table = [input() for _ in range(H)]
p, q = map(int, input().split())

cnt = 0

for i in range(H):
    for j in range(W):
        if i == p and table[i][j] == "#":
            cnt += 1
        elif j == q and table[i][j] == "#":
            cnt += 1
        
print(cnt)
