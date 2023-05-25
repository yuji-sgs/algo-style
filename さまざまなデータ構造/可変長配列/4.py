"""
N 個の整数からなる整数列 A0,A1,…,AN−1が与えられます。
このデータ構造に対して、Q 回のクエリが与えられます。それぞれのクエリに答えてください。 各クエリは、次のいずれかです。

Insert(k,v)：整数値 k,v が与えられるので、数列の左から k 番目の位置に整数値 v を挿入してください
Erase(k)：整数値 k が与えられるので、数列の左から k 番目の整数を削除してください。このとき数列の要素数は 1 だけ減少します
Count(v)：整数値 v が与えられるので、数列中の整数 v の個数を出力してください

これらのクエリの実行例については、入力例 1・出力例 1 を参考にしてください。 なお、最も左の数字は左から 0 番目と数えることにします。
"""

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        k = query[1]
        v = query[2]
        A.insert(k, v)
    elif query[0] == 1:
        k = query[1]
        A.pop(k)
    elif query[0] == 2:
        k = query[1]
        cnt = 0
        for i in range(len(A)):
            if A[i] == k:
                cnt += 1
        print(cnt)
