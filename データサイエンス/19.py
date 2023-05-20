"""
N人が 100 点満点のテストを受けたところ、それぞれの点数は A0,A1,…,AN−1点でした。 
このテストで A0点を取った人のこのテストにおける偏差値を求めるプログラムを作成してください。
"""

N = int(input())
A = list(map(int, input().split()))
mean_A = sum(A) / N  # 平均
sigma_A = (sum((i - mean_A)**2 for i in A) / N) ** 0.5  # 標準偏差

# 偏差値の計算
ans = 50 + 10 * (A[0] - mean_A) / sigma_A

print(ans)
