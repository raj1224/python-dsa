# linear Search
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target  
    return -1  # Return -1 if the target is not found

# Example usage
arr = [1, 2, 3, 4, 5]
target = 3
result = linearSearch(arr, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")    

