"""
N個の整数 A0,A1,…,AN−1が与えられます。
以下の条件をみたす整数の組 (i,j,k) の個数を求めるプログラムを作成してください。
・Ai,Aj,Akの最大値は Ajである。
・0≤i<j<k≤N−1
"""

# データを受け取る
N = int(input())
A = list(map(int, input().split()))

ans = 0
# 変数 x の全探索
for i in range(N):
    # 変数 y の全探索
    for j in range(i + 1, N):
        # 変数 z の全探索
        for k in range(j + 1, N):
            if A[j] == max(A[i], A[j], A[k]):
                ans += 1

# 答えを出力する
print(ans)
