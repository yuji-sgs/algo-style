"""
N 個の文字列 S0,S1,…,SN−1が与えられます。
これらの N 個の文字列の中に同じ 2 つの文字列があるかどうかを判定するプログラムを作成してください。
"""

n = int(input())
s = [input() for _ in range(n)]

flag = False

for i in range(n):
    for j in range(i+1, n):
        if s[i] == s[j]:
            flag = True

if flag:
    print("Yes")
else:
    print("No")
