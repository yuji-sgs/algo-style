"""
英小文字からなる文字列 S と、英小文字 c が与えられます。
文字列 S の中に c が含まれるかどうかを答えるプログラムを作成してください。
"""

S = input()
c = input()

flag = False

for i in range(len(S)):
    if c == S[i]:
        flag = True
    else:
        pass

if flag == True:
    print("Yes")
else:
    print("No")
