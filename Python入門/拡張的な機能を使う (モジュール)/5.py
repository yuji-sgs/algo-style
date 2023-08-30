"""
カメのアルルは、次の問題を考えています。
ある街の選挙で、各有権者が投票した立候補者の名前のリストがあります。
各立候補者が何票ずつ投票されたか、集計して出力してください。
エディタに書かれたコードは、アルルが実際にこの問題に答えたものです。
このコードには誤りが含まれており、実行するとエラーとなります。
collections モジュールのクラスを用いて、正しく動作するようにコードを修正してください。
"""

from collections import defaultdict

# 各有権者が投票した立候補者の名前
votes = ["aruru", "iruru", "ururu", "aruru", "eruru", "oruru", "aruru", "iruru", "aruru", "eruru", "iruru", "ururu", "eruru"]

d = defaultdict(int) # 空の defaultdict インスタンス
for vote in votes: # 投票された立候補者に 1 を足す
    d[vote] += 1

# 投票結果を出力
for name, value in d.items():
    print(f"{name} {value}")
