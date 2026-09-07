from typing import List

class Solution:
    # Function to find the majority element in an array
    def majorityElement(self, nums: List[int]) -> int:
        
        # Size of the given array
        n = len(nums)
        
        # Hash map to store element counts
        mp = {}
        
        # Count occurrences of each element
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        
        """ Iterate through the map to
        find the majority element"""
        for num, count in mp.items():
            if count > n // 2:
                return num
        
        # Return -1 if no majority element is found
        return -1

# Main function to test the Solution class
if __name__ == "__main__":
    arr = [2, 2, 1, 1, 1, 2, 2]
    
    # Create an instance of Solution class
    sol = Solution()
 
    ans = sol.majorityElement(arr)
    
    # Print the majority element found
    print("The majority element is:", ans)
