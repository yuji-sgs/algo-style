"""
N 個の整数 A0,A1,…,AN−1が与えられます。
これらの整数の中から 1 つの整数を選ぶ操作を 2 回行って、それらの積をとります。 そうして得られる N^2個の積の総和を求めてください。
"""

N = int(input())
A = list(map(int,input().split()))

S = sum(A)
print(S*S)
