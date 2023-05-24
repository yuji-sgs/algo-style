"""
N 個の整数からなる整数列 A0,A1,…,AN−1が与えられます。
このデータ構造に対して、Q 回のクエリが与えられます。それぞれのクエリに答えてください。 各クエリは、次のいずれかです。
・　Output(k)：整数値 k が与えられるので、左から k 番目の値を答えてください。ただし k 番目の要素が数列外を参照する場合は Error と出力してください
・　Push(v)：整数値 v が与えられるので、数列の末尾に整数 v を挿入してください
たとえば A=[3,1,4,1] の状態で、クエリ Push(5) を適用すると、A=[3,1,4,1,5] となります。
最も左の数字は左から 0 番目と数えることにします。
"""
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        if query[1] >= len(A):
            print("Error")
        else:
            print(A[query[1]])
    elif query[0] == 1:
        A.append(query[1])
