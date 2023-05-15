"""
N 人が 100 点満点のテストを受けたところ、それぞれの点数は A0,A1,…,AN−1点でした。 
このテストにおける点数の分散 σ2と標準偏差 σ を求めるプログラムを作成してください。
"""

N = int(input())
A = list(map(int, input().split()))

mean = sum(A) / N  # 平均値

disp = sum((i - mean) ** 2 for i in A) / N  # 分散
print(disp)

standard = disp ** 0.5  # 標準偏差
print(standard)
