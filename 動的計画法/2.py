"""
カメのアルルは N 個のマスを使って遊んでいます。
それぞれのマスには数字が 1 つずつ書かれており、マス i には Aiが書かれています。(0≤i≤N−1)
アルルはマス 0 からスタートし、以下のルールに従いながらマス N−1 を目指します。

マス i にたどりつくには次の 2 つの方法がある。(1 ≤ i ≤ N−1)
・ マス i−1 からAi秒かけて移動する。
・ マス i−2 から2Ai秒かけて移動する。
ただし、i が 1 のときは 1 つめの方法のみとることができる。 

アルルがマス N−1 になるべくはやくたどりつくように動きました。
アルルがマス N−1 にたどりついたのは、マス 0 をスタートしてから何秒後か答えてください
"""

N = int(input())
A = list(map(int, input().split()))

dp = [10000] * N
dp[0] = 0
dp[1] = A[1]

for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + 2 * A[i])

print(dp[N - 1])
