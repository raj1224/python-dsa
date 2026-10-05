class LowerBoundFinder:
    # Function to find the lower bound index using binary search
    def lower_bound(self, arr, x):
        low, high = 0, len(arr) - 1     # Search range
        ans = len(arr)                  # Default value if not found

        while low <= high:
            mid = (low + high) // 2     # Find middle index
            if arr[mid] >= x:
                ans = mid               # Store possible answer
                high = mid - 1          # Move to the left
            else:
                low = mid + 1           # Move to the right
        return ans                      # Return result

# Driver code
arr = [3, 5, 8, 15, 19]                # Sorted input array
x = 9                                  # Target value

finder = LowerBoundFinder()           # Create object
ind = finder.lower_bound(arr, x)      # Call method

print("The lower bound is the index:", ind)  # Output result
