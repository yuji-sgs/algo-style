"""
アルルは N 個のボールを持っています。 
ボールには 0 から N-1 までの番号が割り振られており、 ボール i の重さは Wiです。 
また、ボールの重さはそれぞれ異なることがわかっています。
k=0,1,…,N-1 について次の問いに答えてください。
ボール k は何番目に軽いボールですか。
ただし、一番軽いボールを「 0 番目に軽いボール」と呼ぶことにします。
"""

N = int(input())
W = list(map(int, input().split()))
W_sort = sorted(W)

def binary_search(key):
    left = 0
    right = N

    while left < right:
        mid = (left + right) // 2
        if W_sort[mid] >= key:
            right = mid
        else:
            left = mid + 1

    return left

for i in range(N):
    print(binary_search(W[i]))
