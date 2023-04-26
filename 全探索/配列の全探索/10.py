n = int(input())
A = list(map(int, input().split()))

# 線形探索
count = [0] * 9 
for x in A: 
    count[x-1] += 1 

max = count[0]
max_num = 0

for i in range(9):
    if max < count[i]:
        max = count[i]
        max_num = i + 1

print(max_num)
