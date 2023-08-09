"""
1 円玉 と 5 円玉を使って N 円を支払うとき、最低何枚の硬貨が必要ですか。
"""

N = int(input())

ans_5 = N // 5 # 5円で払う枚数
ans_1 = N % 5 # 1円で払う枚数
ans = ans_5 + ans_1

print(ans)
