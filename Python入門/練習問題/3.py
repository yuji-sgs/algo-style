"""
英小文字からなる文字列 S が標準入力で与えられます。
文字列 S に対し、次の操作を行った結果の文字列を出力するプログラムを作成してください。
S の文字を先頭から順に確認し、現れるのが 2 回目以上の文字を * で置き換える。
"""
S = input()

# 受け取った値を利用してコードを書いてください
ans = ""
seen_chars = set()
for s in S:
    if s in seen_chars:
        ans += "*"
    else:
        ans += s
        seen_chars.add(s)

print(ans)
