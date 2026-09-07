class Solution:
    # Function to find union of two sorted arrays using two pointers
    def findUnion(self, arr1, arr2, n, m):
        # List to store union elements
        Union = []

        # Initialize pointers
        i, j = 0, 0

        # Iterate while both pointers are within array bounds
        while i < n and j < m:
            # If element in arr1 is smaller
            if arr1[i] < arr2[j]:
                # Add if empty or not duplicate
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
            # If element in arr2 is smaller
            elif arr2[j] < arr1[i]:
                # Add if empty or not duplicate
                if not Union or Union[-1] != arr2[j]:
                    Union.append(arr2[j])
                j += 1
            else:
                # Elements are equal, add once if not duplicate
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
                j += 1

        # Append remaining elements from arr1
        while i < n:
            if not Union or Union[-1] != arr1[i]:
                Union.append(arr1[i])
            i += 1

        # Append remaining elements from arr2
        while j < m:
            if not Union or Union[-1] != arr2[j]:
                Union.append(arr2[j])
            j += 1

        # Return the union list
        return Union


# Driver code
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    n, m = len(arr1), len(arr2)

    obj = Solution()
    result = obj.findUnion(arr1, arr2, n, m)
    print("Union of arr1 and arr2 is:", *result)
