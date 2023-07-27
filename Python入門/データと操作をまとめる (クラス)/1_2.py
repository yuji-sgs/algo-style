"""
name と age という属性を持つクラス Tortoise を作成し、以下の 4 匹のカメを作成してください。
また、4 匹の名前と年齢をそれぞれ出力してください。
"""

# カメ (Turtoise) クラスとカメの情報を書いてください
class Turtoise:
    def __init__(self, name, age):
        self.name = name
        self.age = age

aruru = Turtoise("aruru", 5)
iruru = Turtoise("iruru", 16)
ururu = Turtoise("ururu", 3)
eruru = Turtoise("eruru", 100)


# カメの名前と年齢を出力
print(f"{aruru.name} は {aruru.age} 歳です。")
print(f"{iruru.name} は {iruru.age} 歳です。")
print(f"{ururu.name} は {ururu.age} 歳です。")
print(f"{eruru.name} は {eruru.age} 歳です。")
