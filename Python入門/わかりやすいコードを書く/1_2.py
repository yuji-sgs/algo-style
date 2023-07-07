"""
1 以上 12 以下の整数 month が標準入力で与えられます。
うるう年ではない年の month 月の日数を出力するプログラムを作成してください。
"""

# 標準入力から値を受け取る
# month: int 型
month = int(input())

# 受け取った値を利用してコードを書いてください
if month == 2:
    print(28)
elif month in [4, 6, 9, 11]:
    print(30)
else:
    print(31)
