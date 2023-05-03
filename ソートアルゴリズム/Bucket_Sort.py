N = int(input())
A = list(map(int, input().split()))

# バケットソート
X = N+1
num = [0] * X
for a in A: num[a] += 1
acc = [0] * X
for idx, count in enumerate(num):
    if idx == 0:
        acc[idx] = count
    else:
        acc[idx] = acc[idx-1] + count
B = [0] * N
for a in A:
    acc[a] -= 1
    B[acc[a]] = a

print(*B)
