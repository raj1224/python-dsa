# Function to find the second smallest element in the array
def secondSmallest(arr, n):
    # Edge case: if the array has fewer than 2 elements
    if n < 2:
        return -1

    small = float('inf')
    second_small = float('inf')

    # Loop through the array to find the second smallest element
    for i in range(n):
        # Update the smallest and second smallest values
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i]

    return second_small  # Return the second smallest element

# Function to find the second largest element in the array
def secondLargest(arr, n):
    # Edge case: if the array has fewer than 2 elements
    if n < 2:
        return -1

    large = float('-inf')
    second_large = float('-inf')

    # Loop through the array to find the second largest element
    for i in range(n):
        # Update the largest and second largest values
        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]

    return second_large  # Return the second largest element

# Driver code
if __name__ == "__main__":
    arr = [1, 2, 4, 7, 7, 5]  # Array of elements
    n = len(arr)  # Size of the array

    # Find the second smallest and second largest elements
    sS = secondSmallest(arr, n)
    sL = secondLargest(arr, n)

    # Output the results
    print(f"Second smallest is {sS}")
    print(f"Second largest is {sL}")