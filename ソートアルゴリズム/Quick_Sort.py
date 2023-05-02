N = int(input())
data = list(map(int, input().split()))

def quick_sort(left, right):
    if left >= right:
        return
    
    i = left
    j = right
    pivot = data[(left + right) // 2]
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
    if left < i-1:
        quick_sort(left, i-1)
    if right > j+1:
        quick_sort(j+1, right)

quick_sort(0, N-1)
print(*data)
