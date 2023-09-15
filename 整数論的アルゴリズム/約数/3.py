"""
正の整数 N であって、N を除く N の約数の総和が N に一致するものを完全数とよびます。
たとえば 6 の約数は 1,2,3,6 であり、6 以外の約数の和は 1+2+3=6 となりますので、6 は完全数です。
与えられた整数 N が完全数かどうかを判定してください。
"""

# 約数列挙
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
divisors = calc_divisors(N)

tmp = sum(divisors[0:len(divisors)-1])
print("Yes" if tmp == divisors[-1] else "No")
