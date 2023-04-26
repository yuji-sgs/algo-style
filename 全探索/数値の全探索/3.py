N = int(input())
if N == 1:
    print("No")
    exit()
for i in range(2, N):
    if N % i == 0:
        print("No")
        exit()
print("Yes")
