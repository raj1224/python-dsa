def bubble_sort(arr, n):
    # Base case: only one element left
    if n == 1:
        return

    did_swap = False  # Flag to detect swap

    # Single pass: move the largest to the end
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            did_swap = True

    # If no swaps occurred, list is already sorted
    if not did_swap:
        return

    # Recurse on the smaller array
    bubble_sort(arr, n - 1)

# Driver code
arr = [13, 46, 24, 52, 20, 9]
print("Before Using Bubble Sort:")
print(arr)

bubble_sort(arr, len(arr))

print("After Using Bubble Sort:")
print(arr)
