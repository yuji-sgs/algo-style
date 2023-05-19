"""
N 人からなる 2 つのグループ A,B があります。 それぞれのグループの合計 2N 人が 100 点満点のテストを受けたところ、
グループ A に属する人の点数はそれぞれ A0,A1,…,AN−1点
グループ B に属する人の点数はそれぞれ B0,B1,…,BN−1点
でした。点数の散らばり具合を四分位範囲を用いて測る場合、どちらのグループの方が点数の散らばりが小さいか求めるプログラムを作成してください。
"""

from statistics import median

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

# 四分位範囲の計算
IQR_A = median(A[(N+1)//2:]) - median(A[:N//2])
IQR_B = median(B[(N+1)//2:]) - median(B[:N//2])

if IQR_A < IQR_B:
    print("A")
elif IQR_B < IQR_A:
    print("B")
else:
    print("same")
