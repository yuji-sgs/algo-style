"""
今、空の連結リスト (nil のみがある状態) から開始して、Q 回のクエリが与えられます。 それぞれのクエリに答えてください。 各クエリは、次のいずれかです。
PushHead(S)：文字列 S 表すノードを先頭 (nil の直後) に挿入してください
PopHead()：先頭 (nil の直後) のノードの文字列を出力して、そのノードを削除してください。ただし連結リストが空である場合は Error と出力してください
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

# 連結リストの先頭にある文字列を返し、その要素を削除する
def erase():
    front = nil.nex
    if front == nil:
        # 連結リストが空なら、Error を返す
        return('Error')
    else:
        ret = front.value   # 先頭の文字列を返す
        nil.nex = front.nex #  先頭を front の次に書き換える
        del front   # メモリを開放する

        return(ret)

# 入力
Q = int(input())
for _ in range(Q):
    query = list(input().split())
    query_type = query[0]

    if query_type == '0':
        S = query[1]
        # ノードを作成する
        v = Node(S)
        insert(v)
    else:
        print(erase())
