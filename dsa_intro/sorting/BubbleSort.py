def bubbleSort(a):
    n = len(a)

    for i in range(n):
        for j in range(0, n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

a = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(a)
print("Sorted array is:", a)