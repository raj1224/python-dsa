class Solution:
    # Function to perform quicksort
    def quickSort(self, arr, low, high):
        # Base case
        if low < high:
            # Partition and get pivot index
            pivotIndex = self.partition(arr, low, high)

            # Sort left part
            self.quickSort(arr, low, pivotIndex - 1)

            # Sort right part
            self.quickSort(arr, pivotIndex + 1, high)

    # Function to partition the array
    def partition(self, arr, low, high):
        # Take pivot as last element
        pivot = arr[high]

        # i will track smaller elements
        i = low - 1

        # Loop through the array
        for j in range(low, high):
            # If element <= pivot
            if arr[j] <= pivot:
                # Move i forward
                i += 1

                # Swap arr[i] and arr[j]
                arr[i], arr[j] = arr[j], arr[i]

        # Put pivot in correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        # Return pivot index
        return i + 1

# Driver code
arr = [10, 7, 8, 9, 1, 5]

# Create object
sol = Solution()

# Call quicksort
sol.quickSort(arr, 0, len(arr) - 1)

# Print sorted array
print(*arr)
