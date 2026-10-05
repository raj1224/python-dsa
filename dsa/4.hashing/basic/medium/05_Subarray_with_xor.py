# 163. Count subarrays with given xor K
# Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.

# Example 1:
# Input : nums = [4, 2, 2, 6, 4], k = 6

# Output : 4

# Explanation : The subarrays having XOR of their elements as 6 are [4, 2],  [4, 2, 2, 6, 4], [2, 2, 6], and [6]




from typing import List
from collections import defaultdict as hashmap
class Solution:
    def subarraysWithXorK(self, nums, k):
        xor, n, ans = 0, len(nums), 0
        mp = hashmap(int)
        for i in range(n):
            xor ^= nums[i]
            if xor == k:
                ans += 1
            target = xor ^ k
            ans += mp[target]
            mp[xor] += 1
        return ans

