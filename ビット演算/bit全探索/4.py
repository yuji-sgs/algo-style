"""
N 個の、英小文字からなる文字列 w0,w1,…,wN-1が与えられます。 
これらの文字列からいくつかを選び、順につなげて作った文章がパングラムであるようにしたいとします。
それが可能となるような「選ぶ文字列の個数」の最小値を答えてください。 
ただし、どのように文字列を選んでもパングラムにならない場合は -1 と出力してください。
"""

N = int(input())
w = list(input().split())

ans = -1

for i in range(1 << N):
    # 選ぶ単語数
    num_words = 0
    # 対応する選び方で作れる文字列
    build_str = ""
    for j in range(N):
        if (i >> j) & 1:
            num_words += 1
            build_str += w[j]
    
    if len(set(build_str)) == 26:
        if ans == -1:
            ans = num_words
        else:
            ans = min(ans, num_words)

print(ans)
