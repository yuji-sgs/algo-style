"""
英小文字からなる文字列 S が与えられます。
文字列 S 中に「連続する 2 文字が同じ文字である箇所」が何個あるかを答えるプログラムを作成してください。
"""

S = input()

count = 0


for i in range(len(S) - 1):
    if S[i] == S[i+1]:
        count += 1

print(count)
