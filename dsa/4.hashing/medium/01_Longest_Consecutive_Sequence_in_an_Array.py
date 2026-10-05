# 128. Longest Consecutive Sequence

# Given an unsorted integer array nums, possibly containing duplicate values. Consecutive values do not need to occupy adjacent positions in the array. Find the length of the longest sequence of distinct consecutive integers.

# Example 1
# Input: nums = [100, 4, 200, 1, 3, 2, 2, 5]

# Output: 5

# Explanation: The values 1, 2, 3, 4, 5 form the longest consecutive sequence. The duplicate 2 does not increase its length.

# Example 2
# Input: nums = [0, -1, 1, 2, -2, 4]

# Output: 5

# Explanation: The longest sequence is -2, -1, 0, 1, 2, so its length is 5


class Solution:
    def longestConsecutive(self, nums):
        vals = set(nums)
        long_seq = 0
        for val in vals:
            if val-1 in vals:
                continue
            cnt_seq = 1
            next_val = val+1
            while next_val in vals:
                next_val += 1
                cnt_seq += 1
            long_seq = max(long_seq,cnt_seq) 
        return long_seq