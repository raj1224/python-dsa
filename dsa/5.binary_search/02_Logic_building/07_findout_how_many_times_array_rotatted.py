# 765. Find out how many times the array is rotated
# Given an integer array nums of size n, sorted in ascending order with distinct values. The array has been right rotated an unknown number of times, between 0 and n-1 (including). Determine the number of rotations performed on the array.

# Example 1:
# Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]

# Output: 4

# Explanation: The original array should be [0, 1, 2, 3, 4, 5, 6, 7]. So, we can notice that the array has been rotated 4 times.

import sys

class Solution:

    def findKRotation(self, nums: list[int]) -> int:
        # Initialize the low pointer to the beginning
        low = 0
        # Initialize the high pointer to the end
        high = len(nums) - 1
        # Track the minimum value found, starting with a very large number
        ans = sys.maxsize
        # Track the index of the minimum value found
        index = -1
        
        # Loop until the search space is exhausted
        while low <= high:
            # If the current search space is fully sorted
            if nums[low] <= nums[high]:
                # Check if the first element is the overall minimum
                if nums[low] < ans:
                    # Update the answer and index
                    ans = nums[low]
                    index = low
                # Break early since the rest of the elements will only be larger
                break
                
            # Calculate the middle point of the current search space
            mid = low + (high - low) // 2
            
            # Check if the left half is sorted
            if nums[low] <= nums[mid]:
                # Check if the smallest element in the left half is a new minimum
                if nums[low] < ans:
                    # Update the index and the minimum value
                    index = low
                    ans = nums[low]
                # Discard the left half and search the right half
                low = mid + 1
            # Otherwise, the right half must be sorted
            else:
                # Check if the smallest element in the right half is a new minimum
                if nums[mid] < ans:
                    # Update the index and the minimum value
                    index = mid
                    ans = nums[mid]
                # Discard the right half and search the left half
                high = mid - 1
                
        # Return the final index which represents the number of rotations
        return index

# driver code starts
if __name__ == "__main__":
    solution = Solution()
    
    nums = [4, 5, 6, 7, 0, 1, 2]
    
    result = solution.findKRotation(nums)
    
    print(result)