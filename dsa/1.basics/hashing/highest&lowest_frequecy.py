# Find the highest/lowest frequency element

# Problem Statement: Problem Statement: Given an array of size N. Find the highest and lowest frequency element.

class FrequencyCounter:
    def Frequency(self, arr):
        freq_map = {}                # Dictionary to store frequency of each element

        # Count frequencies
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        maxFreq = 0
        minFreq = len(arr)
        maxEle = 0
        minEle = 0

        # Iterate through dictionary to find max and min frequency elements
        for element, count in freq_map.items():
            if count > maxFreq:
                maxFreq = count
                maxEle = element

            if count < minFreq:
                minFreq = count
                minEle = element

        # Print results
        print("The highest frequency element is:", maxEle)
        print("The lowest frequency element is:", minEle)


if __name__ == "__main__":
    fc = FrequencyCounter()
    arr = [10, 5, 10, 15, 10, 5]
    fc.Frequency(arr)


# 2nd method
class Solution:
    # Function to get the highest
    # occurring element in array n
    def mostFrequentElement(self, nums):
        # Variable to store maximum frequency
        maxFreq = 0
        
        # Variable to store element
        # with maximum frequency
        maxEle = 0
        
        # HashMap
        mpp = {}
        
        # Iterating on the array
        for num in nums:
            # Updating hashmap
            if num in mpp:
                mpp[num] += 1
            else:
                mpp[num] = 1
        
        # Iterate on the map
        for ele, freq in mpp.items():
            if freq > maxFreq:
                maxFreq = freq
                maxEle = ele
            elif freq == maxFreq:
                maxEle = min(maxEle, ele)
        
        # Return the result
        return maxEle