# 62. Find minimum in Rotated Sorted Array
# Given an integer array nums of size N, sorted in ascending order with distinct values, and then rotated an unknown number of times (between 1 and N), find the minimum element in the array.

# Example 1:
# Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]

# Output: 0

# Explanation: Here, the element 0 is the minimum element in the array.

class Solution:
    def findMin(self, nums: list[int]) -> int:
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
