class Solution:
    # Function to find the minimum element using linear search
    def findMin(self, nums):

        # Initialize answer with a large number
        min_val = float('inf')

        # Traverse each element
        for i in range(len(nums)):

            # Update minimum value
            min_val = min(min_val, nums[i])

        # Return the result
        return min_val

# Input array
nums = [4, 5, 6, 7, 0, 1, 2]

# Create object of Solution
sol = Solution()

# Call function and store result
result = sol.findMin(nums)

# Output the result
print("Minimum element is", result)


# OPTIMAL SOLUTION
class Solution:
    # Function to find the minimum element using binary search
    def findMin(self, nums):

        # Initialize low and high pointers
        low, high = 0, len(nums) - 1

        # Binary search loop
        while low < high:

            # Calculate mid index
            mid = low + (high - low) // 2

            # Check which half to discard
            if nums[mid] > nums[high]:

                # Minimum lies in right half
                low = mid + 1

            else:

                # Minimum lies in left half (including mid)
                high = mid

        # Return the minimum element
        return nums[low]

# Input array
nums = [4, 5, 6, 7, 0, 1, 2]

# Create object of Solution
sol = Solution()

# Call function and store result
result = sol.findMin(nums)

# Output the result
print("Minimum element is", result)
