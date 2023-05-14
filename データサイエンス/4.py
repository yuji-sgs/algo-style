"""
N 人が 100 点満点のテストを受けたところ、それぞれの点数は A0,A1,…,AN−1点でした。 
このテストにおける点数の最頻値 AMoを求めるプログラムを作成してください。
"""

N = int(input())
A = list(map(int, input().split()))

# 要素の個数をカウントする
cnt = [0] * 101
for a in A:
    cnt[a] += 1

# 最も多く出てくる要素の個数 ma を求める
ma = max(cnt)

# 要素の個数 が ma の要素を出力する
for i in range(101):
    if cnt[i] == ma:
        print(i)
