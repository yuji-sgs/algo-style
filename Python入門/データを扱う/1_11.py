"""
a, b, c からなる文字列 S が標準入力で与えられます。
文字列 S に操作 (★) を行った結果の文字列を T とし、
文字列 T に操作 (★) を行った結果の文字列を U とし、
文字列 U に操作 (★) を行った結果の文字列を V とします。
文字列 T,U,V を改行区切りで出力するプログラムを作成してください。
"""

# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
def translate_string(S):
    # 初期化
    T = ""
    # 文字列をループ
    for s in S:
        # 条件に合わせて文字を変換
        if s == "a":
            T += "b"
        elif s == "b":
            T += "c"
        elif s == "c":
            T += "a"
    return T
    
T = translate_string(S)
U = translate_string(T)
V = translate_string(U)

print(T)
print(U)
print(V)
