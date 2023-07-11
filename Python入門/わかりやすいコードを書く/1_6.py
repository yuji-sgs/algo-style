"""
カメのアルルは、次の問題を考えています。

配列 names にカメの名前がたくさん与えられます。
この中に、アルルとアララに似た名前がそれぞれいくつあるか数え出力してください。

ただし、アルル (aruru) に似た名前とは、

文字列の 2,4 文字目が同じ
文字列の 3,5 文字目が同じ
である名前です。

また、アララ (arara) に似た名前とは、
文字列の 2,4 文字目が同じ
文字列の 1,3,5 文字目がすべて同じ
である名前です。

エディタに書かれているコードは、アルルが実際にこの問題に答えたものです。
しかし、このコードには実装上の誤りが含まれています。
誤りを修正し、正しく動作するプログラムを作成してください。
"""

# このコードの誤りを修正してください

# カメは全員アルファベット 5 文字の名前です
names = [ "alulu", "umumu", "namae", "totot", "irisu", "aaaaa", "mamma", "dadaa", "wowow", "kanan", "usasa", "kamem", "erina", "choco", "betty", "xoooo" ]

# アルルに似た名前を数える変数
answer_aruru = 0

# アララに似た名前を数える変数
answer_arara = 0

# アルルに似た名前とアララに似た名前を数える
for name in names:
    if name[1] == name[3]:
        if name[2] == name[4]:
            answer_aruru += 1
            if name[0] == name[2] and name[2] == name[4]:
                answer_arara += 1

# 答えを出力する         
print(answer_aruru)
print(answer_arara)
