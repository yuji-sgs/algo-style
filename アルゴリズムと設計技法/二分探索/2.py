"""
アルルは今年銀行に N 円を預けています。 銀行に預けたお金は、利子がついて 1 年ごとに X 倍になります。利子がついたあとの金額は整数でない可能性もあります。
アルルは今年も含めて 1 年ごとに、追加で 1 円ずつ預けます。 預金額が 5 年後に M 円になるような X を求めて出力してください。
なお、アルルは 5 年後にも 1 円を預けるものとします。
また、出力値の絶対誤差 (想定解と出力の差の絶対値) は 0.01 まで許されます。
"""

N, M = map(int, input().split())

# Xの初期値を仮定して、二分探索で求める
left = 0.0
right = 100

# 許容誤差0.01で二分探索
while right - left > 1e-9:
    mid = (left + right) / 2

    # 5年後の預金額を計算する
    total = N + 1
    for i in range(5):
        total = total * mid + 1

    # 5年後の預金額が目標より大きい場合、Xの上限を下げる
    if total > M:
        right = mid
    # そうでない場合、Xの下限を上げる
    else:
        left = mid

print(left)
