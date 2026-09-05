class Solution:
    def rotateArrayByOne(self, nums):
        # Store the first element in a temporary variable
        temp = nums[0]
        
        # Shift elements to the left
        for i in range(1, len(nums)):
            nums[i - 1] = nums[i]
        
        # Place the first element at the end
        nums[-1] = temp

# Main method for testing
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    
    solution.rotateArrayByOne(nums)
    
    print(nums)  # Output the rotated array