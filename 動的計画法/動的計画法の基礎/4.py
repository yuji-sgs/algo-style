"""
カメのアルルは壁にタイルを敷き詰めようとしています。
壁は縦幅 1 、横幅 N の長方形です。
タイルの形状は以下の 3 種類があります。

・ 縦の長さが 1、横の長さが 1 の正方形
・ 縦の長さが 1、横の長さが 2 の長方形
・ 縦の長さが 1、横の長さが 3 の長方形

壁にタイルを敷き詰める方法は全部で何通りありますか。 ただし、同じ種類のタイルは区別しないものとします。 また、タイルを回転させたり重ねて貼ることはできません。
"""

N = int(input())

dp = [0] * (N + 1) # 動的計画法として計算しやすくするため(N+1)
dp[0] = 1

for i in range(1, N + 1):
    dp[i] += dp[i - 1]  # 横長さ1のタイルを追加
    if i - 2 >= 0:
        dp[i] += dp[i - 2]  # 横長さ2のタイルを追加
    if i - 3 >= 0:
        dp[i] += dp[i - 3]  # 横長さ3のタイルを追加

print(dp[N])
