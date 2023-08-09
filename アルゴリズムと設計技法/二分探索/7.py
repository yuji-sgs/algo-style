"""
カメのアルルは今日から毎日貯金をすることにしました。
具体的には、今日を 1 日目として、次のような貯金計画を立てました。
1 日目に 1 円、2日目に 2 円、…といった具合で、i 日目に i 円を貯金する。

アルルは貯金をどれだけ続けると目標額にたどりつけるのか気になっています。
k=0,1,…,N-1 について次の問いに答えてください。
貯金額がはじめてXk円以上になるのは何日目ですか。
"""

N = int(input())
X = list(map(int, input().split()))

def func(x):
    return x * (x + 1) // 2

def binary_search(key):
    left = 0
    right = 10 ** 18
    while left < right:
        mid = (left + right) // 2
        if func(mid) >= key:
            right = mid
        else: 
            left = mid + 1
    return left
 
for i in range(len(X)):
    print(binary_search(X[i]))
