def kaibun(x):
    s = str(x)
    flag = True
    n = len(s)
    for i in range(n):
        if s[i] != s[(n-1)-i]:
            flag = False
    return flag

l, r = map(int, input().split())

count = 0

for x in range(l,r+1):
    if kaibun(x):
        count += 1

print(count)
