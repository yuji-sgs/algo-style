"""
for 文と range () を適切に用いて、1 以上 100 以下 の整数の合計値を求めるプログラムを作成してください。
"""

ans = 0
for i in range(1, 101):
    ans += i

print(ans)
