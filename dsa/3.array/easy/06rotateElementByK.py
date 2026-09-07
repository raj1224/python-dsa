# BETTER APPROACH

class Solution:
    # Rotate the array to the right by k positions
    def rotateRight(self, arr, k):
        n = len(arr)
        if n == 0:
            return

        k %= n

        # Store last k elements
        temp = arr[-k:]

        # Shift the remaining elements
        for i in range(n - k - 1, -1, -1):
            arr[i + k] = arr[i]

        # Copy stored elements to the front
        for i in range(k):
            arr[i] = temp[i]

    # Rotate the array to the left by k positions
    def rotateLeft(self, arr, k):
        n = len(arr)
        if n == 0:
            return

        k %= n

        # Store first k elements
        temp = arr[:k]

        # Shift remaining elements
        for i in range(k, n):
            arr[i - k] = arr[i]

        # Copy stored elements to the end
        for i in range(k):
            arr[n - k + i] = temp[i]


# Driver code
sol = Solution()

arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
sol.rotateRight(arr, k)
print("Array after right rotation:", arr)

arr2 = [1, 2, 3, 4, 5, 6, 7]
sol.rotateLeft(arr2, k)
print("Array after left rotation:", arr2)





# OPTIMAL APPROACH
class Solution:
    # Helper function to reverse part of array between two indices
    def reverse(self, nums, start, end):
        # Swap elements from start to end
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Function to rotate array left or right by k steps
    def rotateArray(self, nums, k, direction):
        # Get length of array
        n = len(nums)

        # Edge case: no rotation needed
        if n == 0 or k == 0:
            return nums

        # Normalize k if it's larger than n
        k = k % n

        # If direction is right
        if direction == "right":
            # Step 1: reverse the entire array
            self.reverse(nums, 0, n - 1)

            # Step 2: reverse first k elements
            self.reverse(nums, 0, k - 1)

            # Step 3: reverse remaining n-k elements
            self.reverse(nums, k, n - 1)

        # If direction is left
        elif direction == "left":
            # Step 1: reverse first k elements
            self.reverse(nums, 0, k - 1)

            # Step 2: reverse remaining n-k elements
            self.reverse(nums, k, n - 1)

            # Step 3: reverse entire array
            self.reverse(nums, 0, n - 1)

        # Return rotated array
        return nums

# Driver code
sol = Solution()

# Input values
nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
direction = "right"

# Perform rotation
result = sol.rotateArray(nums, k, direction)

# Print result
print(result)
