n = int(input())

count = 0

for i in range(n + 1):
    if (i % 2 != 0) & (i % 3 != 0) & (i % 5 != 0):
        count += 1

print(count) 
