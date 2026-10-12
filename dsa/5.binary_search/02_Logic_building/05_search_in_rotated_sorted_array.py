# 112. Search in rotated sorted array-II
# Given an integer array nums, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.

# Example 1:
# Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3

# Output: True

# Explanation: The element 3 is present in the array. So, the answer is True.

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        k=target

        while low <= high:
            mid = (low + high) // 2

            # If mid is the target
            if nums[mid] == k:
                return True

            # Cannot determine sorted half due to duplicates
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= k <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                if nums[mid] <= k <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False

