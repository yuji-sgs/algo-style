"""
2 以上の整数 N が与えられます。
N 以下の整数のうち、最大の素数を答えてください。
"""

def is_prime(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True

N = int(input())
if is_prime(N):
    print(N)
else:
    for i in range(N, 0, -1):
        if is_prime(i):
            print(i)
            exit()
