def SelectionSort(a):
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

a = [64, 25, 12, 22, 11]
SelectionSort(a)
print("Sorted array is:", a)