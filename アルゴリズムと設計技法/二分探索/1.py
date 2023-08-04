"""
整数 N が与えられます。 次の式を満たす0 以上 100 以下の実数 X を求めてください。
X(X(X+1)+2)+3 = N
また、絶対誤差 (想定解と出力の差の絶対値) は 0.01 まで許されます。
"""

def func(X):
    return X*(X*(X+1)+2)+3

def binary_search(key):
    left = 0.0
    right = 100.0
    eps = 1e-4 # 許容誤差

    while right - left > eps:
        mid = (left + right) / 2
        if func(mid) == key:
            return mid
        elif func(mid) < key:
            left = mid
        else:
            right = mid
    return mid

N = int(input())
ans = binary_search(N)
print(ans)
