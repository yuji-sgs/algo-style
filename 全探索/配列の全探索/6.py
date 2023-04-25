n = int(input())
A = list(map(int, input().split()))

max = A[0]
i = 0

for i in range(n):
    if max < A[i]:
        max = A[i]

print(max)
