"""
カメのアルルは、1 つの箱と N 個のボールを持っています。
ボールには 0 から N−1 までの番号が振られており、 ボール i の重さは Wiです。
アルルは箱にいくつかのボールを、重さの合計が M となるよう番号の小さい方から順に入れようと考えています。
このようなボールの入れ方は存在するか答えてください。
"""

# 入力
N, M = map(int, input().split())
W = list(map(int, input().split()))

# (N+1) × (M+1) のマスを用意する
dp = [[False] * (M+1) for _ in range(N+1)]

# 初期状態 (左上のマスにコマがありうる)
dp[0][0] = True

# 各マス (i, j) から「真下」「右下」へコマを渡していく
for i in range(N):
    for j in range(M+1):
        # マス (i, j) にコマがいく可能性がない場合はスキップ
        if not dp[i][j]:
            continue

        # 真下マスへコマを渡す
        dp[i+1][j] = True

        # 右下マス (あるならば) へコマを渡す
        if j+W[i] <= M:
            dp[i+1][j+W[i]] = True

# 答え
print('Yes' if dp[N][M] else 'No')
