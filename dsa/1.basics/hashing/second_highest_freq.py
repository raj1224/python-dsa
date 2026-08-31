class Solution:
    """Function to get the second highest 
    occurring element in array"""
    def secondMostFrequentElement(self, nums):
        
        # Variable to store the size of array
        n = len(nums)
        
        """Variable to store maximum frequency
        and second Max frequency"""
        maxFreq = 0
        secMaxFreq = 0
        
        """Variable to store elements with most 
        and second most frequency"""
        maxEle = -1
        secEle = -1
        
        # Visited array
        visited = [False] * n
        
        # First loop
        for i in range(n):
            # Skip second loop if already visited
            if visited[i]:
                continue
            
            """Variable to store frequency
            of current element"""
            freq = 0
            
            # Second loop
            for j in range(i, n):
                if nums[i] == nums[j]:
                    freq += 1
                    visited[j] = True
            
            """Update variables if new element  
            having highest frequency or second
            highest frequency is found"""
            if freq > maxFreq:
                secMaxFreq = maxFreq
                maxFreq = freq
                secEle = maxEle
                maxEle = nums[i]
            elif freq == maxFreq:
                maxEle = min(maxEle, nums[i])
            elif freq > secMaxFreq:
                secMaxFreq = freq
                secEle = nums[i]
            elif freq == secMaxFreq:
                secEle = min(secEle, nums[i])
        
        # Return the result
        return secEle

if __name__ == "__main__":
    nums = [4, 4, 5, 5, 6, 7]
    
    """Creating an instance of 
    Solution class"""
    sol = Solution()
    
    """Function call to get the second
    highest occurring element in array"""
    ans = sol.secondMostFrequentElement(nums)
    
    print(f"The second highest occurring element in the array is: {ans}")
