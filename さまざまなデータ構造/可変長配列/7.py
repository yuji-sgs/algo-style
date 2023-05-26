"""
N 個の整数からなる整数列 A0,A1,…,AN−1が与えられます。
このデータ構造に対して、Q 回のクエリが与えられます。それぞれのクエリに答えてください。 各クエリは、次のいずれかです。
・PushFront(v)：整数値 v が与えられるので、数列の先頭に整数 v を挿入してください
・PopFront()：数列の先頭の整数値を出力し、さらに数列の先頭の値を削除してください。ただし数列が空の状態でこのクエリが呼ばれたときは Error と出力してください。このとき数列には何もしません
これらのクエリの実行例については、入力例 1・出力例 1 を参考にしてください。
"""

# 入力
N = int(input())
A = list(map(int, input().split()))

A.reverse()

Q = int(input())
for i in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]

    if query_type == 0:
        # pushfront クエリ
        v = query[1]
        A.append(v)
    elif query_type == 1:
        # popfront クエリ
        if len(A) > 0:
            print(A.pop())
        else:
            print('Error')
