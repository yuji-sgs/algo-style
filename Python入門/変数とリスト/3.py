"""
エディタに書かれているコードは、日曜日から土曜日までの曜日を表す英文字列を格納したリスト型の変数 DAY_OF_WEEK を用意し、配列そのものを出力するものです。
このコードを変更し、次の通り出力するプログラムを作成してください。
ただし、日曜日を前から 0 番目の曜日と数えることとします。

1 行目: 日曜日を表す英文字列
2 行目: 水曜日を表す英文字列
3 行目: 配列の最後に格納されている (土曜日を表す) 英文字列
"""

DAY_OF_WEEKS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print(DAY_OF_WEEKS[0])
print(DAY_OF_WEEKS[3])
print(DAY_OF_WEEKS[-1])
