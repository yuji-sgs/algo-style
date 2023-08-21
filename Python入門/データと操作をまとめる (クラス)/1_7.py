class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __eq__(self, other): # 等号の動作を定義するメソッド
        return self.first == other.first and self.second == other.second
    # ここに小なり演算子を書いてください
    def __lt__(self, other):
        if self.first != other.first:   # first が違う数なら first を比較する
            return self.first < other.first
        else:                           # first が同じ数なら second を比較する
            return self.second < other.second

a = Pair(2, 3)
b = Pair(1, 4)
c = Pair(1, 3)
print(a < b)
print(b < c)
print(c < b)
