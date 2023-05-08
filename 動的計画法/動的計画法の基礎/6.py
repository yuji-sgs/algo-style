"""
カメのアルルはすごろく盤とサイコロを使ってすごろくで遊んでいます。

すごろく盤には N+1 個のマスがあり、 0 から N までの番号が振られています。
アルルはマス 0 からスタートし、ゴールのマス N を目指します。
また、サイコロは D0,D1,…,DM−1の M 種類の出目が等確率で出ます。
アルルはサイコロを振り、出た目の数だけ進むことを繰り返します。

このすごろくでは、ゴールのマスにちょうどたどりつかないとあがることはできません。
アルルがこのすごろくであがる可能性があるか答えてください。
"""

N, M = map(int, input().split())
D = list(map(int, input().split()))

# 動的計画法の舞台となる配列
dp = [False] * (N + 1)

# マス 0 にははじめから到達している
dp[0] = True

# 順に計算していく
for i in range(1, N + 1):
    for j in range(M):
        if i - D[j] >= 0 and dp[i - D[j]]:
            dp[i] = True

print("Yes" if dp[N] else "No")
