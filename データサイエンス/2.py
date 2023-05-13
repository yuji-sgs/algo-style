"""
N 人が 100 点満点のテストを受けたところ、それぞれの点数は A0,A1,…,AN−1点でした。 
このテストにおける点数の平均値 (=平均点)A- を求めるプログラムを作成してください。
"""

N = int(input())
A = list(map(int, input().split()))

# 平均の計算
mean = sum(A) / len(A)

print(mean)
