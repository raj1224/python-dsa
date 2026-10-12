# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

def first(l,h,t,nums,res):
     while l <= h:
            m = (l+h)//2
            if nums[m] == t:
                res = m
                h = m-1
            elif nums[m]<t:
                l = m+1
            else:
                h = m-1
     return res
def last(l,h,t,nums,res):
    while l <= h:
            m = (l+h)//2
            if nums[m] == t:
                res = m
                l = m+1
            elif nums[m]<t:
                l = m+1
            else:
                h = m-1
    return res
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = -1
        l,h,t = 0,n-1,target
        return [first(l,h,t,nums,res),last(l,h,t,nums,res)]
        
        
       