"""
空の連結リスト (nil のみがある状態) から開始して、Q 回のクエリが与えられます。 それぞれのクエリに答えてください。 各クエリは、次のいずれかです。
Insert(S)：文字列 S を新たに挿入してください (nil の直後に挿入してください)
Output(k)：連結リストを先頭ノード (nil の直後のノード) から開始して k 個分の文字列を順に一行に出力してください。ただし途中で nil ノードに到達した場合は処理を打ち切ります
"""

# 連結リストの各ノード
class Node:
    def __init__(self, value=''):
        self.nex = None  # 次がどのノードを指すか
        self.value = value  # ノードに付随している値

# 連結リストの初期化
nil = Node()
nil.nex = nil

# 連結リストへ先頭への要素の挿入
def insert(v):
    v.nex = nil.nex;  # v の次を、現在の先頭に
    nil.nex = v;  # 先頭を v に書き換える

# 入力
Q = int(input())
for _ in range(Q):
    typ, S = input().split()
    if typ == '0':
        # ノードを作成する
        v = Node(S)
        insert(v)
    else:
        # 先頭から k (=S) 個
        v = nil # nilは連結リストの先頭を示すノード
        for i in range(int(S)):
            v = v.nex; # vに次のノードを代入
            if v == nil:
                break
            print(v.value, end=' ')
        print()
