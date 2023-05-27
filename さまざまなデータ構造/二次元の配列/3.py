"""
縦 H マス、横 W マスからなるマス目上の地図があります。 各マスには英小文字のいずれかが描かれています。
この地図の、上から x マス目、左から y マス目を中心とした 縦横 3 マスを表示するプログラムを作成してください。 ただし、左上のマスを上から 0 マス目、左から 0 マス目であるとします。
"""

H, W, x, y = map(int, input().split())
table = [input() for _ in range(H)]

for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
        print(table[i][j], end = "")
    print()
