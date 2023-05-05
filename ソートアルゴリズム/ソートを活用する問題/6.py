"""
カメのアルルは今日 N 個の授業を受けようとしています。
現在は時刻 0 で、授業 i は時刻Liに始まり、時刻Riに終わります。 授業間の移動時間は 0 であるとして良いですが、授業に遅れて入室することや、早めに退出することはできません。
アルルは N 個の授業すべてを受けられるでしょうか。
"""

N = int(input())

time_table = []
for i in range(N):
    L, R = map(int, input().split())
    time_table.append((L, R))

time_table.sort(key=lambda x:x[0])

flg = True

for i in range(1, N):
    if time_table[i-1][1] >= time_table[i][1]:
        flg = False
        break

if flg == True:
    print("Yes")
else:
    print("No")
        
