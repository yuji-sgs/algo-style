"""
正の整数 N が与えられます。
N の正の約数の個数を求めてください。
"""

def calc_divisors(N):
    divisors = []
    for i in range(1, N + 1):
        # √N で打ち切り
        if i * i > N:
            break
        
        # i が N の約数でない場合はスキップ
        if N % i != 0:
            continue

        # i は約数である
        divisors.append(i)

        # N ÷ i も約数である (重複に注意)
        if N // i != i:
            divisors.append(N // i)

    # 約数を小さい順に並び替えて出力
    divisors.sort()
    return divisors

N = int(input())
print(len(calc_divisors(N)))
