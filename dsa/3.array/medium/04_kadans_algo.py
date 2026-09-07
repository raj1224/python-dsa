from typing import List

class Solution:
    # Function to find maximum sum of subarrays
    def maxSubArray(self, nums: List[int]) -> int:
        
        # maximum sum
        maxi = float('-inf') 
        
        # current sum of subarray
        sum = 0 
        
        # Iterate through the array
        for i in range(len(nums)):
            
            # Add current element to the sum
            sum += nums[i] 
            
            # Update maxi if current sum is greater
            if sum > maxi:
                maxi = sum 
            
            # Reset sum to 0 if it becomes negative
            if sum < 0:
                sum = 0 
        
        # Return the maximum subarray sum found
        return maxi

if __name__ == "__main__":
    arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]

    # Create an instance of Solution class
    sol = Solution()

    maxSum = sol.maxSubArray(arr)

    # Print the max subarray sum
    print(f"The maximum subarray sum is: {maxSum}")
