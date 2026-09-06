class Solution:
    # Function to find the element that appears only once
    def getSingleElement(self, arr):
        n = len(arr)

        # Check each element's count
        for i in range(n):
            num = arr[i]
            count = 0

            # Count how many times num appears
            for j in range(n):
                if arr[j] == num:
                    count += 1

            # Return if it appears exactly once
            if count == 1:
                return num

        return -1  # fallback

# Driver code
arr = [4, 1, 2, 1, 2]
obj = Solution()
ans = obj.getSingleElement(arr)
print("The single element is:", ans)
