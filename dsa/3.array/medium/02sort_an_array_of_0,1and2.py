class Solution:
    # Function to sort the array containing only 0s, 1s and 2s
    def sortZeroOneTwo(self, nums):
        # Initialize count variables for 0s, 1s, and 2s
        count0 = count1 = count2 = 0

        # Count the frequency of 0s, 1s, and 2s
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        # Overwrite the array with sorted values
        index = 0

        # Fill with 0s
        for _ in range(count0):
            nums[index] = 0
            index += 1

        # Fill with 1s
        for _ in range(count1):
            nums[index] = 1
            index += 1

        # Fill with 2s
        for _ in range(count2):
            nums[index] = 2
            index += 1

# Driver code
nums = [1, 0, 2, 1, 0]
obj = Solution()
obj.sortZeroOneTwo(nums)
print(nums)


# OPTIMAL APPROACH: Dutch National Flag Algorithm
class Solution:
    # Function to sort list containing 0s, 1s, and 2s using Dutch National Flag Algorithm
    def sortZeroOneTwo(self, nums):
        # Initialize three pointers: low and mid at 0, high at end
        low, mid, high = 0, 0, len(nums) - 1

        # Traverse until mid crosses high
        while mid <= high:
            # If element is 0, swap with low, move both low and mid forward
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            # If element is 1, just move mid forward
            elif nums[mid] == 1:
                mid += 1
            # If element is 2, swap with high, move only high backward
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Driver code
nums = [2, 0, 2, 1, 1, 0]
obj = Solution()
obj.sortZeroOneTwo(nums)
print(nums)
