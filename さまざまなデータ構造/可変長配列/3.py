"""
N 個の整数からなる整数列 A0,A1,…,AN−1が与えられます。
このデータ構造に対して、Q 回のクエリが与えられます。それぞれのクエリに答えてください。 各クエリは、次のいずれかです。
・　Push(v)：整数値 v が与えられるので、数列の末尾に整数 v を挿入してください
・　Pop()：数列の末尾の整数値を出力し、さらに数列の末尾の値を削除してください。ただし数列が空の状態でこのクエリが呼ばれたときは Error と出力してください。このとき数列には何もしません
たとえば A=[3,1,4,1] の状態で、クエリ Push(5) を適用すると、A=[3,1,4,1,5] となります。
最も左の数字は左から 0 番目と数えることにします。
"""

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        A.append(query[1])
    elif query[0] == 1:
        if len(A) > 0:
            print(A.pop())
        else:
            print("Error")
