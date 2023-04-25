n = int(input())
A = list(map(int, input().split()))

min = A[0]

for i in range(n):
    if min > A[i]:
        min = A[i]

print(min)
