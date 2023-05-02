N = int(input())
A = list(map(int, input().split()))

for k in range(1, N):
    pos = k
    while pos > 0 and A[pos-1] > A[pos]:
        A[pos-1], A[pos] = A[pos], A[pos-1]
        pos -= 1
    print(*A)
