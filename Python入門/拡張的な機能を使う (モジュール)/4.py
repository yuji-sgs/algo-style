"""
次の条件を満たす 3 つの正の整数の組 (a,b,c) をピタゴラス数といいます。
・a^2+b^2=c^2
a,b,c がいずれも 1 以上 20 以下であるようなピタゴラス数 (a,b,c) をすべて出力してください。
"""

import itertools # itertools モジュールを読み込む

# 3 重 for 文を itertools.product で書き直す
for a, b, c in itertools.product(range(1, 21), repeat=3):
    if a**2 + b**2 == c**2: # ピタゴラス数の条件を満たすなら出力
        print(a, b, c)
