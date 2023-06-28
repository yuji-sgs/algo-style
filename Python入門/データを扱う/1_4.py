"""
1 以上 100 以下の数字に対応する英単語 S が標準入力で与えられます。
S が 1 以上 10 以下の数字に対応する英単語の場合はその値を数字に変換し、そうでない場合は −1 を出力するプログラムを作成してください。
"""

# 標準入力から値を受け取る
# S: str 型
S = input()

# 英単語をキーとし、対応する数字を値とする辞書型の変数
numbers_dict = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10
}

# 入力された英単語が辞書に含まれていれば、その値を出力し、そうでなければ -1 を出力する
if S in numbers_dict:
    print(numbers_dict[S])
else:
    print(-1)
