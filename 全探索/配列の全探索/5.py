n = int(input())
A = list(map(int, input().split()))

sum = 0

for i in range(1,n):
    if A[i-1] < A[i]:
        sum += 1

print(sum)  
