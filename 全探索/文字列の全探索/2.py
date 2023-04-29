"""
英小文字からなる文字列 S が与えられます。
文字列 S が回文かどうかを判定するプログラムを作成してください。 なお文字列 S が回文であるとは、S を逆から読んでも S になることを言います。
"""

# データを受け取る
S = input()

# S の長さを取得する
N = len(S)

# 線形探索
flag = True
for i in range(N):
    if S[i] != S[-(1+i)]:
        flag = False

# 答えを出力する
if flag: print("Yes")
else: print("No")
