"""
正の整数 N,M が与えられます。
3 つの正の整数の組 x,y,z であって、
x,y,z はそれぞれ 1 以上 N 以下の整数である
x,y,z の総和は M 以下である
という条件をともに満たすものが何個あるかを求めてください。
"""

N, M = map(int, input().split())

# 答えを表す変数
ans = 0

# x, y を動かして、z の範囲を考える
for x in range(1, N + 1):
    for y in range(1, N + 1):
        # z のとりうる最大値
        max_z = min(N, M - x - y)

        # max_z <= 0 のとき、条件を満たす z はない
        if max_z <= 0: 
            continue

        # z は 1 以上 max_z 以下をとりうる
        ans += max_z;

print(ans)
