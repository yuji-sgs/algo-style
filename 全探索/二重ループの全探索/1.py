n = int(input())
A = list(map(int, input().split()))
count = 0

for x in A:
    if x == 1:
        continue
    elif x == 2:
        count += 1
        continue
    #print(x)
    for i in range(2, x):
        if x%i == 0:
            break
    else:
        count += 1
print(count)
