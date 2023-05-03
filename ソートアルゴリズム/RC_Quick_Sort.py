import random

N = int(input())
data = list(map(int, input().split()))

def randomized_quick_sort(left, right):
    if left >= right:
        return

    i = left
    j = right

    # ピボットをランダムに選択
    pivot_index = random.randint(left, right)
    pivot = data[pivot_index]

    while True:
        while data[i] < pivot:
            i = i + 1
        while data[j] > pivot:
            j = j - 1
        if i >= j:
            break
        data[i], data[j] = data[j], data[i]
        i = i + 1
        j = j - 1

    randomized_quick_sort(left, i-1)
    randomized_quick_sort(j+1, right)

randomized_quick_sort(0, N-1)
print(*data)
