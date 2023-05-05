"""
あるクラスには N 人の生徒がいます。 各生徒の出席番号は 0,1,…,N−1 です。 出席番号が i である生徒のことを、生徒 i と呼ぶことにします。 生徒 i の名前は Siで、身長は hiです。
この生徒たちが次の条件を満たすように一列に並びました (いわゆる背の順です)。

どの生徒i についても、生徒i の前にいる生徒は、次のいずれかの条件を満たす
・生徒 iよりも、身長が小さい
・生徒iと身長が等しく、出席番号が小さい

一列に並んだ状態において、 生徒 X の 1 つ前にいる生徒と 1 つ後ろにいる生徒の名前を答えてください。
"""

N, X = map(int, input().split())
Students = []
for i in range(N):
    S, h = input().split()
    Students.append((i, S, int(h)))


# 身長の昇順、出席番号の昇順でソート
Students.sort(key=lambda x: (x[2], x[0]))

# 出席番号がXの人を見つける
X_index = None
for i in range(N):
    if X == Students[i][0]:
        X_index = i
        break

# 前後の生徒の名前を出力
print(Students[X_index - 1][1])
print(Students[X_index + 1][1])
