# 素因数分解
def prime_factorization(N):
    i = 2
    factors = []
    while i * i <= N: # これ以上の i を試す必要がない
        if N % i: # 割り切れないなら
            i += 1
        else:
            N //= i
            factors.append(i)
    if N > 1: # ループを抜けた後、もし N が1より大きいならば
        factors.append(N)
    return factors

N = int(input())
print(*prime_factorization(N))
