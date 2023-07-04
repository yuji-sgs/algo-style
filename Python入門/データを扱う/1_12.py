"""
シーザー暗号は、英小文字からなる文字列に対するシンプルな暗号方式の 1 つです。
シーザー暗号では、文字列 S の各文字を 3 つ前の文字に置き換えることで暗号化します。

英小文字からなる文字列 S が標準入力で与えられます。
S をシーザー暗号で暗号化した文字列 T を出力するプログラムを作成してください。
"""

def caesar_cipher(S):
    # 置き換えるための文字列を作成
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # 暗号化された文字列を初期化
    T = ""

    # 文字列Sをループ
    for s in S:
        # 現在の文字の位置を取得
        index = alphabet.index(s)
        # 3つ前の文字の位置を計算（アルファベットを循環させるために、26で割った余りを取る）
        new_index = (index - 3) % 26
        # 新しい文字を暗号化された文字列に追加
        T += alphabet[new_index]

    return T

# 標準入力から文字列Sを取得
S = input()
print(caesar_cipher(S))
