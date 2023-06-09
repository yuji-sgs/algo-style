"""
エディタに書かれている関数 tax_included(price, rate) は、「税抜価格が price 円の商品に rate % の税率がかかる場合の税込価格」を整数値で返すものです。
整数 X が標準入力で与えられるので、この関数を利用して、 税抜価格が X 円の商品に 10 % の税率がかかる場合の税込価格を整数値で出力するプログラムを作成してください。
"""

# 税込価格を計算する関数
# price: int 型
# rate: int 型
# 返り値: int 型
def tax_included(price, rate):
    return price * (100 + rate) // 100

# 標準入力から受け取る
# X: int 型
X = int(input())

# 受け取った値を利用してコードを書いてください
print(tax_included(X, 10))
