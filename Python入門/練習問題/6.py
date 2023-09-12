# どこまでの整数を足したかを記録する変数を用意
count = 0

# 足した整数の合計値を記録する変数を用意
total = 0

# total が 10000 を超えるまで処理を繰り返す
while total <= 10000:
    count += 1      # 足す整数を 1 増やす
    total += count    # 合計値に加える

# 答えを出力
print(count)
