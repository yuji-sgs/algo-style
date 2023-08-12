"""
N 個の品物があり、それぞれ 0,1,…,N−1 と番号が振られています。 
品物 i の重さは Wiであり、価値は Viです。
これらの品物からいくつか選び、選んだ品物の価値の総和をなるべく大きくしたいとします。 
ただし選んだ品物の重さの総和が M 以下でなければなりません。
選んだ品物の価値の総和の最大値を求めてください。
"""

N, M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

ans = 0

for i in range(1 << N):
    sum_w = 0
    sum_v = 0
    for j in range(N):
        if (i >> j) & 1:
            sum_w += W[j]
            sum_v += V[j]

    if sum_w <= M: # 重さがM以下の場合、更新
        ans = max(ans, sum_v)

print(ans)
