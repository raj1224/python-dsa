# 178. Longest subarray with sum K
# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.

# Example 1:
# Input: nums = [10, 5, 2, 7, 1, 9],  k=15

# Output: 4

# Explanation:

# The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.



class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        l,r = 0,0
        max_len = 0
        sum = nums[0]
        while r < n:
            while l<=r and sum > k:
                sum -= nums[l]
                l += 1

            if sum == k:
                max_len= max(max_len,r-l+1)
            r += 1
            if r<n :
                sum += nums[r]

        return max_len
