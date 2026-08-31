class Solution:
    # Function to reverse the array in-place
    def reverseArray(self, arr):
        # Initialize pointer to the beginning of the array
        p1 = 0

        # Initialize pointer to the end of the array
        p2 = len(arr) - 1

        # Loop until the two pointers meet in the middle
        while p1 < p2:
            # Swap the elements at p1 and p2
            arr[p1], arr[p2] = arr[p2], arr[p1]

            # Move the left pointer one step to the right
            p1 += 1

            # Move the right pointer one step to the left
            p2 -= 1

# Driver code
if __name__ == "__main__":
    # Create a Solution object
    sol = Solution()

    # Input array
    arr = [1, 2, 3, 4, 5]

    # Call the reverse function
    sol.reverseArray(arr)

    # Print the reversed array
    print(" ".join(map(str, arr)))

# BRUTE FORCE APPROACH
class Solution:
    #  Function to reverse an array
    def reverseArray(self, arr):
        # Get the length of the input array
        n = len(arr)

        # Create a new array of same size to store reversed elements
        ans = [0] * n

        # Start a loop to fill ans[] from the back of arr[]
        for i in range(n):
            # Place elements from the end of arr into the start of ans
            ans[i] = arr[n - 1 - i]

        # Return the reversed array
        return ans

# Driver code
if __name__ == "__main__":
    # Create an object of the Solution class
    obj = Solution()

    # Input array
    arr = [1, 2, 3, 4, 5]

    # Call the reverseArray function
    result = obj.reverseArray(arr)

    # Print the result
    print("Reversed Array:", result)

# BUILT-IN FUNCTION APPROACH
class Solution:
    # Function to reverse the array using slicing
    def reverseArray(self, arr):
        # Reassign the array with reversed version using slicing
        arr[:] = arr[::-1]

# Driver code
if __name__ == "__main__":
    # Input array
    arr = [1, 2, 3, 4, 5]

    # Create Solution object
    obj = Solution()

    # Call reverse function
    obj.reverseArray(arr)

    # Output the reversed array
    print(" ".join(map(str, arr)))
