"""
N 個の整数からなる整数列 A0,A1,…,AN−1が与えられます。
このデータ構造に対して、Q 回のクエリが与えられます。それぞれのクエリに答えてください。 各クエリは、次のいずれかです。
・　PushFront(v)：整数値 v が与えられるので、数列の先頭に整数 v を挿入してください
・　PushBack(v)：整数値 v が与えられるので、数列の末尾に整数 v を挿入してください
・　Get(k)：整数値 k が与えられるので、数列の左から k 番目の値を答えてください。ただし k 番目の要素が数列外を参照する場合は Error と出力してください
最も左の数字は左から 0 番目と数えることにします。 また、これらのクエリの実行例については、入力例 1・出力例 1 を参考にしてください。
"""

# 入力
N = int(input())
A = list(map(int, input().split()))

# A の先頭に挿入される要素を管理する list
A_front = []

Q = int(input())
for i in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]

    if query_type == 0:
        # pushfront クエリ (A_front の末尾に挿入する)
        # A_front の末尾にある要素が全体の先頭になることに注意
        v = query[1]
        A_front.append(v)
    
    elif query_type == 1:
        # pushback クエリ (A の末尾に挿入する)
        v = query[1]
        A.append(v)
    
    elif query_type == 2:
        k = query[1]
        # get クエリ
        if k < len(A_front):
            # k が A_front のサイズより小さいならば、A_front の末尾から k 番目を出力する
            print(A_front[-(k+1)])
        else:
            # そうでないならば、A の先頭から k' 番目を出力する (範囲外なら Error と表示)
            k -= len(A_front)
            if k < len(A):
                print(A[k])
            else:
                print('Error')
