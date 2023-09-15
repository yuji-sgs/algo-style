"""
56 の正の約数が何個あるかを答えてください。
"""
list = []
for i in range(1, 57):
    if 56 % i == 0:
        list.append(i)

print(len(list))
