"""
3 つの整数 A,B,C が標準入力で与えられます。
B の値が A 以上かつ、B の値が C 未満ならば　Yes と、そうでないならば No と出力するプログラムを作成してください。
"""
# 標準入力から値を受け取る
# A, B, C: int 型
A = int(input())
B = int(input())
C = int(input())

# 受け取った値を利用してコードを書いてください
if A <= B and B < C:
    print("Yes")
else:
    print("No")
