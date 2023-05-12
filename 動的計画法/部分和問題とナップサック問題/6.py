"""
カメのアルルは、N 枚のカードを持っています。
カードには 0 から N−1 までの番号が振られており、 カード i には整数 Xiが書かれています。
アルルはいくつかのカードを、書かれた数の合計が「 A で割った余りが B となる数」となるように選ぼうと考えています。 (カードを 1 枚も選ばなくても問題ありません。)
このようなカードの選び方は存在するか答えてください。
"""

# 入力
N, A, B = map(int, input().split())
W = list(map(int, input().split()))

# (N+1) x A の配列を用意する
# 配列全体を false で初期化する
dp = [[False] * A for _ in range(N+1)]

# 初期状態
dp[0][0] = True

# ループ
for i in range(N):
    for j in range(A):
        # マス (i, j) へ到達不能の場合はスキップ
        if not dp[i][j]:
            continue

        # 更新
        dp[i+1][j] = True
        dp[i+1][(j+W[i])%A] = True

# 答え
print('Yes' if dp[N][B] else 'No')
