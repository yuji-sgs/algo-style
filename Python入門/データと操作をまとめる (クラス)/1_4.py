class Tortoise:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # ここに greet メソッドを書いてください
    def greet(self, name):
        print("Hello, {}! I'm {}.".format(name, self.name))

aruru = Tortoise("aruru", 5)
aruru.greet("iruru") # アルルがイルルに挨拶する
