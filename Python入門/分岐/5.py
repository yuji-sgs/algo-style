"""
あるパズルゲームでは、各ステージに 1 以上 30 以下の整数の難易度が割り振られています。
ステージは難易度に応じて easy, normal, hard, special の 4 種類に分類されています。

難易度が 1 以上 9 以下の場合: easy
難易度が 11 以上 19 以下の場合: normal
難易度が 21 以上 29 以下の場合: hard
難易度がそれ以外 (10,20,30) の場合: special
問題の難易度 diff が標準入力から与えられます。

この問題の種類を答えるプログラムを作成してください。
"""
# 標準入力から値を受け取る
# diff: int 型
diff = int(input())

# 受け取った値を利用してコードを書いてください
if 1 <= diff <= 9:
    print("easy")
elif 11 <= diff <= 19:
    print("normal")
elif 21 <= diff <= 29:
    print("hard")
else:
    print("special")
