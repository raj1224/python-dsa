class Solution:
    # Function to sort the array using insertion sort
    def insertionSort(self, nums):
        n = len(nums) # Size of the array 
        
        # For every element in the array 
        for i in range(1, n):
            key = nums[i] # Current element as key 
            j = i - 1
            
            # Shift elements that are greater than key by one position
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            
            nums[j + 1] = key # Insert key at correct position
        
        return nums

if __name__ == "__main__":
    # Create an instance of solution class
    solution = Solution()
    
    nums = [13, 46, 24, 52, 20, 9]
    
    print("Before Using Insertion Sort:")
    for num in nums:
        print(num, end=" ")
    print()
    
    # Function call for insertion sort
    nums = solution.insertionSort(nums)
    
    print("After Using Insertion Sort:")
    for num in nums:
        print(num, end=" ")
    print()