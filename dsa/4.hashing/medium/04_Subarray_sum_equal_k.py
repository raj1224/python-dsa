# 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
 
        prefix_sum = 0
        count = 0
 
        for value in nums:
            prefix_sum += value
            needed_sum = prefix_sum - k

            count += prefix_count.get(needed_sum, 0)
 
            prefix_count[prefix_sum] = (
                prefix_count.get(prefix_sum, 0) + 1
            )
 
        return count