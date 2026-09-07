# Function to check if the array is sorted
def isSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:  # If any element is smaller than the previous one, return false
            return False
    return True  # Return true if the array is sorted

# Driver code
arr = [1, 2, 3, 4, 5]
n = len(arr)

# Output result
print("True" if isSorted(arr, n) else "False")
