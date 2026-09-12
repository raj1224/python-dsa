class UpperBoundFinder:
    # Binary search to find upper bound
    def upper_bound(self, arr, x):
        low, high = 0, len(arr) - 1
        ans = len(arr)  # Default to length if no element > x

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > x:
                ans = mid      # Store current mid as answer
                high = mid - 1 # Search left
            else:
                low = mid + 1  # Search right
        return ans

# Driver code
arr = [3, 5, 8, 9, 15, 19]
x = 9

finder = UpperBoundFinder()
ind = finder.upper_bound(arr, x)

print("The upper bound is the index:", ind)
