"""
2 つの整数 L,R が与えられます。
L 以上 R 以下の整数の中から、 一の位が等しくなるように相異なる 2 つの整数を選ぶ方法は何通りあるか求めるプログラムを作成してください。
"""

# データを受け取る
L, R = map(int, input().split())

count = 0
# 変数 i の全探索
for i in range(L,R+1):
    # 変数 j の全探索
    for j in range(i+1,R+1):
        if i % 10 == j % 10:
            count += 1

# 答えを出力する
print(count)
