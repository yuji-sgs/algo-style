n = int(input())
A = list(map(int, input().split()))

sum = 0

for i in A:
    if i > 0:
        sum += 1
    else:
        pass

print(sum)
