"""
西暦 2123 年 3 月 28 日は日曜日ですか。
日曜日ならば Yes を、そうでないならば No を出力するプログラムを作成してください。
"""

import datetime # datetime モジュールを読み込む

# 2123 年 3 月 28 日を表す変数
d = datetime.date(2123, 3, 28)
weekday = d.weekday()

# ここにコードを書いてください
if weekday == 6:
    print("Yes")
else:
    print("No")
