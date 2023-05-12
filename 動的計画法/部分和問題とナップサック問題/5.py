"""
カメのアルルは、1 つの箱と N 個のボールを持っています。
ボールには 0 から N−1 までの番号が振られており、 ボール i の重さは Wiです。アルルは箱にできるだけ少ない個数のボールを、重さの合計が M となるよう入れようと考えています。
アルルがボールを入れ終わったとき、箱に入っているボールの個数を答えてください。ただし、このようなボールの入れ方が存在しない場合は -1 と答えてください。
"""

N, M = map(int, input().split())
W = list(map(int, input().split()))

# 最小化問題のため、要素を大きい値で初期化
INF = 100000
dp = [[INF] * (M+1) for _ in range(N+1)]

# 初期状態は0
dp[0][0] = 0

for i in range(N):
    for j in range(M+1):

        # 不可能な場合はスキップ
        if dp[i][j] == INF:
            continue
        
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

        if j+W[i] <= M:
            dp[i+1][j+W[i]] = min(dp[i][j+W[i]], dp[i][j] + 1)

print(dp[N][M] if dp[N][M] != INF else -1)
