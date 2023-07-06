"""
エディタに書かれているコードは、辞書型の変数が格納されたリスト型の変数 person_info を用意し、配列そのものを出力するものです。
ここで、person_info に格納された辞書は人の情報を表しており、次の 3 つのキーを持ちます。
person_info に格納された辞書のそれぞれに、BMI を表すデータを追加し、person_info を出力するプログラムを作成してください。
ただし、キーは BMI とし、 値は round() 関数を用いて丸め、小数第 1 位まで表すこととします。
"""

person_info = [
    {"name": "aruru", "height": 1.7, "weight": 70.0},
    {"name": "iruru", "height": 1.6, "weight": 65.0},
    {"name": "ururu", "height": 1.8, "weight": 70.0},
    {"name": "eruru", "height": 1.5, "weight": 40.0}
]

# ここに person_info を加工するコードを書いてください
for d in person_info:
    bmi = d["weight"] / d["height"] ** 2
    d["BMI"] = round(bmi, 1)

# person_info を出力
print(person_info)
