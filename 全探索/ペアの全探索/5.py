"""
長さ N の文字列 S が与えられます。
以下の条件をみたす整数の組 (x,y) の個数を数えるプログラムを作成してください。
・S の x 文字目と y 文字目は等しい
・0≤x<y≤N−1
ただし、S の先頭の文字が 0 文字目であるとします。
"""

n = int(input())
s = input()

count = 0

for x in range(n):
    for y in range(x+1, n):
        if s[x] == s[y]:
            count += 1

print(count)
