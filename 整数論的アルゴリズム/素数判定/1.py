"""
1 以上の整数 N が与えられます。
整数 N が素数かどうかを判定してください。(O(N))
"""

def is_prime(N):
    if N < 2:
        return False
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

N = int(input())
print("Yes" if is_prime(N) else "No")
