"""
カメのアルルは、次の問題を考えています。

1 以上 10 以下の整数 n が標準入力で与えられます。
n が素数ならば Yes を、素数でないならば No を出力するプログラムを作成してください。
"""

# 1 以上 10 以下の整数 n を受け取って、
# n が素数ならば True を、素数でないならば False を返す関数
def is_prime(n):
    if n == 1:
        return False  # True を False に修正
    elif n == 2:
        return True
    elif n == 3:
        return True
    elif n == 4:
        return False
    elif n == 5:
        return True
    elif n == 6:
        return False
    elif n == 7:  # 2 を 7 に修正
        return True
    elif n == 8:
        return False
    elif n == 9:
        return False
    else:
        return False

# 標準入力から値を受け取る
# n: int 型
n = int(input())

# 関数の返り値に応じて、答えを出力する
if is_prime(n):
    print("Yes")
else:
    print("No")
