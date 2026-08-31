def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        min_index = i  # Assume current index is the minimum

        # Find the minimum element in the remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update min_index if smaller is found

        # Swap the found minimum with the first element of unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

    # Print the sorted array
    print("After selection sort:")
    print(*arr)


# Driver code
arr = [13, 46, 24, 52, 20, 9]

# Print array before sorting
print("Before selection sort:")
print(*arr)

# Call selection sort
selection_sort(arr)
