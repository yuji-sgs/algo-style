"""
エディタに予め記入されているリスト型定数 ZODIAC は十二支の動物名を平仮名で格納したものです。
動物名を表す平仮名 S が標準入力で与えられます。 S が十二支リストに含まれる場合は Yes と、そうでない場合は No と出力するプログラムを作成してください。
"""

# 標準入力から値を受け取る
# S: str 型
S = input()

# 十二支の動物名を平仮名で格納したリスト
ZODIAC = [
    "ねずみ", "うし", "とら", "うさぎ", "たつ", "へび",
    "うま", "ひつじ", "さる", "にわとり", "いぬ", "いのしし" 
]

Flag = False

for i in range(len(ZODIAC)):
    if S == ZODIAC[i]:
        Flag = True
    else:
        continue

if Flag == True:
    print("Yes")
else:
    print("No")
