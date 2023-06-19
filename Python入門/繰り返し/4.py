"""
1 桁の掛け算を順番に行い、次のように結果を 81 行で表示するプログラムを作成してください。
"""

for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i*j))
