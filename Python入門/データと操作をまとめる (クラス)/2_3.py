class Character:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def attack(self, other): # 相手を攻撃するメソッド
        if self.hp <= 0:            # 自分の HP が 0 なら何もしない
            return
        other.hp -= self.strength   # 自分の攻撃力と同じだけ相手の HP を減らす
        if other.hp <= 0:           # 相手の HP が 0 以下になったら 0 にする
            other.hp = 0

# ここに Character クラスを継承したクラス Healer を書いてください
class Healer(Character):
    # max_hp 属性を追加する
    def __init__(self, name, hp, strength):
        super().__init__(name, hp, strength)
        self.max_hp = hp
    def heal(self): # 自分の HP を回復するメソッド
        self.hp = self.max_hp
    def attack(self, other): # HP が低ければ回復するように変更する
        if self.hp <= self.max_hp / 2:
            self.heal()
        else:
            super().attack(other)

# HP を出力するメソッド
def print_hp(character1, character2):
    print(f"{character1.name}: {character1.hp}, {character2.name}: {character2.hp}")

# Character クラスのインスタンス aruru
aruru = Character("aruru", 60, 30)
# Healer クラスのインスタンス iruru
iruru = Healer("iruru", 70, 25)

print_hp(aruru, iruru) # HP を出力
for i in range(2): # 2 回交互に攻撃する
    aruru.attack(iruru) # aruru が iruru に攻撃する
    print(f"{aruru.name}の攻撃！")
    print_hp(aruru, iruru)
    iruru.attack(aruru) # iruru が aruru に攻撃する
    print(f"{iruru.name}の攻撃！")
    print_hp(aruru, iruru)
