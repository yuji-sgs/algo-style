"""
N 人が 100 点満点のテストを受けたところ、それぞれの点数は A0,A1,…,AN−1点でした。 
このテストにおける点数について、第 1 四分位数 Q1、中央値A~、 第 3 四分位数 Q3をそれぞれ求めるプログラムを作成してください。
"""

from statistics import median
N = int(input())
A = list(map(int,input().split()))
A.sort()

# 四分位数を出力
print(median(A[:N//2]), median(A), median(A[(N+1)//2:]))
