"""
サイズ H×W の盤面が与えられます。 これらの盤面の各マスには、文字 o か x が描かれています。
この盤面内の o の描かれたマスの個数を求めてください。
"""
# 入力
H, W = map(int, input().split())
table = [input() for _ in range(H)]

# 答えを表す変数
ans = 0

# i, j を動かして、盤面の文字を取得する
for i in range(H):
    for j in range(W):
        # i 行目 j 文字目
        c = table[i][j]
        if c == 'o':
            ans += 1

print(ans)
