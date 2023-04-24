n, v = map(int, input().split())
A = list(map(int, input().split()))

sum = 0

for i in range(n):
    if A[i] == v:
        sum += 1
    else:
        pass

print(sum)
