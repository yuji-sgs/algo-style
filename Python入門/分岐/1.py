"""
カメのアルルの年齢を表す整数 age が標準入力で与えられます。
if-else 構文を適切に用いることで、
もしアルルが 20 歳以上なら You can drink! と出力し、
そうでないなら You can't drink. と出力する
プログラムを作成してください。
"""

# 標準入力から値を受け取る
# age: int 型
age = int(input())

# 受け取った値を利用してコードを書いてください
if age >= 20: # もし age が 20 以上なら
    print("You can drink!")
else: # そうでないなら
    print("You can't drink.")
