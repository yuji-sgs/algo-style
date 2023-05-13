N = int(input())
A = list(map(int, input().split()))

x_0 = 0
x_1 = 0
x_2 = 0
x_3 = 0
x_4 = 0

for i in range(N):
    if 0 <= A[i] <= 20:
        x_0 += 1
    elif 21 <= A[i] <= 40:
        x_1 += 1
    elif 41 <= A[i] <= 60:
        x_2 += 1
    elif 61 <= A[i] <= 80:
        x_3 += 1
    else:
        x_4 += 1

print(x_0)
print(x_1)
print(x_2)
print(x_3)
print(x_4)
