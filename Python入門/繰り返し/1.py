"""
エディタに書かれているコードは、整数値が格納されたリスト型の変数 numbers を用意し、配列そのものを出力するものです。
for 文を適切に用いてこのコードを変更し、numbers の要素の合計値を出力するプログラムを作成してください。
"""

numbers = [3, 14, 15, 92, 65, 35]

sum = 0

for number in numbers:
    sum += number

print(sum)
