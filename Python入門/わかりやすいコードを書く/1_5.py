"""
整数 n,x が標準入力で与えられます。
エディタに書かれているコードのうち関数の部分を変更して、 「1 ページあたりの人数が n 人のとき、x ページ目に表示されるのは何位から何位までか」を表示するプログラムを作成してください。
"""

# x ページ目に表示されるのは何位から何位までかを返す関数
def paginate(n, x):
    return n * x - (n-1), n * x

# 標準入力から値を受け取る
# n: int 型
# x: int 型
n = int(input())
x = int(input())

# 答えを求め、出力する
first, last = paginate(n, x)
print(f"{first} ~ {last}")
