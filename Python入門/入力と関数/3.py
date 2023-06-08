"""
エディタに書かれているコードは、Hello! という文字列と World! という文字列を順番に出力する関数 hello() を定義したものです。
この関数を利用して、Hello! と World! を交互にそれぞれ 5 回ずつ出力するプログラムを作成してください。
"""

# "Hello" と "World!" を交互に出力する関数
def hello():
    print("Hello!")
    print("World!")

for _ in range(5):
    hello()
