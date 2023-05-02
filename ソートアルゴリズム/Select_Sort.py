N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
    min_A = i
    for k in range(i+1, N):
        if A[k] < A[min_A]:
            min_A = k 
    A[i], A[min_A] = A[min_A], A[i]
    print(*A)
