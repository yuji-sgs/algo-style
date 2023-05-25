"""
N 個の整数からなる整数列 A0,A1,…,AN−1が与えられます。
このデータ構造に対して、Q 回のクエリが与えられます。それぞれのクエリに答えてください。 各クエリは、次のいずれかです。
Reverse()：数列全体を左右反転してください
Push(v)：整数値 v が与えられるので、数列の末尾に整数 v を挿入してください
Pop()：数列の末尾の整数値を出力し、さらに数列の末尾の値を削除してください。ただし数列が空の状態でこのクエリが呼ばれたときは Error と出力してください。このとき数列には何もしません
これらのクエリの実行例については、入力例 1・出力例 1 を参考にしてください。
"""

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        A.reverse()
    elif query[0] == 1:
        v = query[1]
        A.append(v)
    elif query[0] == 2:
        if len(A) > 0:
            print(A[-1])
            A.pop(-1)
        else:
            print("Error")
