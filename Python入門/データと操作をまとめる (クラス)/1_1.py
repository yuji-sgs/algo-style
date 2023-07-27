"""
名前が "eruru"、年齢が 100 歳である Tortoise クラスの変数 eruru を作成してください。
また、名前と年齢を (名前) は (年齢) 歳です。 という形式で出力してください。
"""

# カメ (Tortoise) クラスの定義
class Tortoise:
    name = ""
    age = 0

# ここに eruru の情報を書いてください
eruru = Tortoise()
eruru.name = "eruru"
eruru.age = 100

# 名前と年齢を出力
print(f"{eruru.name} は {eruru.age} 歳です。")
