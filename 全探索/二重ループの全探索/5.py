# 回文数か判定する関数
def is_palindrome(x):
    flag = True
    n = len(x)
    for i in range(n):
        if s[i] != s[(n-1)-i]:
            flag = False
    return flag

N = int(input())

cnt = 0

for j in range(N):
    s = input()
    if is_palindrome(s):
        cnt += 1

print(cnt)
