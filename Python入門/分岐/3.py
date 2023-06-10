"""
if-elif-else 構文を用いて、次の要件を満たすプログラムを作成してください。
カメのアルルの年齢を表す整数 age を標準入力から受け取り、
アルルが 15 歳未満なら child と出力する
アルルが 15 歳以上 65 歳未満なら working-age と出力する
アルルが 65歳以上なら senior と出力する
"""

# 標準入力から値を受け取る
# age: int 型
age = int(input())

# 受け取った値を利用してコードを書いてください
if age < 15:
    print("child")
elif 15 <= age < 65:
    print("working-age")
else:
    print("senior")
