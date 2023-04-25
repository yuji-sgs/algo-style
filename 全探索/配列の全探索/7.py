n = int(input())
A = list(map(int, input().split()))

max = A[0]
max_num = 0

for i in range(n):
    if max < A[i]:
        max = A[i]
        max_num = i

print(max_num)
