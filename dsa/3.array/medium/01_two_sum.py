class Solution:
    # Function to check if any two numbers sum up to target (variant 1)
    def two_sum_exists(self, arr, target):
        n = len(arr)
        # Outer loop picks one element at a time
        for i in range(n):
            # Inner loop searches for another element that complements arr[i]
            for j in range(i + 1, n):
                # If sum equals target, return "YES"
                if arr[i] + arr[j] == target:
                    return "YES"
        # No pair found that sums to target
        return "NO"

    # Function to return indices of two numbers that sum to target (variant 2)
    def two_sum_indices(self, arr, target):
        n = len(arr)
        # Outer loop picks one element at a time
        for i in range(n):
            # Inner loop searches for another element that complements arr[i]
            for j in range(i + 1, n):
                # If sum equals target, return the pair of indices
                if arr[i] + arr[j] == target:
                    return [i, j]
        # No such pair found
        return [-1, -1]

if __name__ == "__main__":
    sol = Solution()

    arr = [2, 6, 5, 8, 11]
    target = 14

    # Variant 1
    print(sol.two_sum_exists(arr, target))

    # Variant 2
    print(sol.two_sum_indices(arr, target))
