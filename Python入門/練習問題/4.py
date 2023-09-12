S = input()
T = input()

# 一致している文字の数を格納するための変数を用意
count = 0

# S と T の先頭の文字から調べる
for i in range(8):
    if S[i] == T[i]: # S の i 文字目と T の i 文字目が一致しているかを判定する
        count += 1


# 答えを出力
if count >= 4:
    print("Bad")
else:
    print("Good")
