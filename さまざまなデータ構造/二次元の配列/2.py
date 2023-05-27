"""
サイズ H×W の盤面が 2 つ与えられます。 これらの盤面の各マスには、文字 o か x が描かれています。
各盤面に対して、上から x 行目 (最上行を 0 行目とする)、左から y 列目 (最左列を 0 列目とする) のマスを (x,y) と表すことにします。
このとき 2 つの盤面の違い度を、 2 つの盤面で描かれた文字が異なるようなマス (x,y) の個数として定義します。 与えられた 2 つの盤面の違い度を求めてください。
"""

H, W = map(int, input().split())
table1 = [input() for _ in range(H)]
table2 = [input() for _ in range(H)]

cnt = 0

for x in range(H):
    for y in range(W):
        if table1[x][y] != table2[x][y]:
            cnt += 1

print(cnt)
