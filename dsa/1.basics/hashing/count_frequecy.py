# Count frequency of each element in the array

# Problem Statement: Given an array, we have found the number of occurrences of each element in the array.



from collections import defaultdict

class Solution:
    # Function to count frequency of each element in the array using defaultdict
    def Frequency(self, arr, n):
        # Create a defaultdict to store frequency of each element
        freq_map = defaultdict(int)

        # Traverse the array and count frequencies
        for i in range(n):
            freq_map[arr[i]] += 1

        # Traverse through the defaultdict and print frequencies
        for key, value in freq_map.items():
            print(key, value)

if __name__ == "__main__":
    # Input array
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)

    # Create Solution instance
    sol = Solution()

    # Call the function to count frequencies
    sol.Frequency(arr, n)
