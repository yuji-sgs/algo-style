"""
1 以上 10 以下の数字 num が標準入力で与えられます。
num を英語に直して出力するプログラムを作成してください。
"""

# 標準入力から値を受け取る
# num: int 型
num = int(input())

# 添字に対応する英語を格納したリスト
ENGLISH_NUM = [
    "", # そのまま取得できるようダミーの文字列で添字をずらす
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten"
]

# 答えを出力する
print(ENGLISH_NUM[num])
