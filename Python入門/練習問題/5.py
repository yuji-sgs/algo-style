# 上の行から順番に模様を作る
for i in range(8):
    row = "" # 今の行の模様を格納する
    for j in range(8):
        if (i+j) % 2 == 0: # i+j の値が偶数なら "."
            row += "."
        else: # i+j の値が奇数なら "#"
            row += "#"
    print(row)
