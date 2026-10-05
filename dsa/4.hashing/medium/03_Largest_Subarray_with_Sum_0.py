# 766. Largest Subarray with Sum 0
# You are given an integer array arr of size n which contains both positive and negative integers. Your task is to find the length of the longest contiguous subarray with sum equal to 0.

# Return the length of such a subarray. If no such subarray exists, return 0.

# Example 1:
# Input: arr = [15, -2, 2, -8, 1, 7, 10, 23]

# Output: 5

# Explanation:

# The subarray [-2, 2, -8, 1, 7] sums up to 0 and has the maximum length among all such subarrays.


from typing import List
from collections import defaultdict

class Solution:
    def maxLen(self, n: int, arr: List[int]) -> int:
        temp, mp = 0, defaultdict(int)
        ans = 0
        for i in range(len(arr)):
            temp += arr[i]
            if temp == 0:
                ans = i+1
            elif temp in mp:
                ans = max(ans, i - mp[temp])
            if temp not in mp:
                mp[temp] = i
        return ans