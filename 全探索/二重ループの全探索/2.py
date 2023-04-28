def count_yaku(x):
    yaku = 0
    for i in range(1, x+1):
        if x % i == 0:
            yaku += 1
    return yaku

n, k = map(int, input().split())

sum = 0

for x in range(1, n+1):
    if count_yaku(x) == k:
        sum += 1

print(sum)
