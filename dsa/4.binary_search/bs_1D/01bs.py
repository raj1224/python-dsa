# iterrative approach to binary search

class Solution:
    # Function to perform Binary Search on sorted list
    def binarySearch(self, nums: [int], target: int) -> int:
        n = len(nums)  # size of the array
        low = 0
        high = n - 1

        # Keep searching until low crosses high
        while low <= high:
            mid = (low + high) // 2  # Find the middle index
            if nums[mid] == target:
                return mid  # Target found
            elif target > nums[mid]:
                low = mid + 1  # Search in right half
            else:
                high = mid - 1  # Search in left half
        return -1  # Target not found


if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]  # sorted list
    target = 6  # target element to search

    obj = Solution()  # Create object of Solution class
    ind = obj.binarySearch(a, target)

    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind)


# RECURSIVE APPROACH TO BINARY SEARCH

class Solution:
    # Recursive Binary Search function
    def binarySearch(self, nums: [int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1  # Base case: target not found

        # Find middle index
        mid = (low + high) // 2

        # If target is found at mid
        if nums[mid] == target:
            return mid
        # If target is greater, search right half
        elif target > nums[mid]:
            return self.binarySearch(nums, mid + 1, high, target)
        # Otherwise, search left half
        return self.binarySearch(nums, low, mid - 1, target)

    # Public function to initiate search
    def search(self, nums: [int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)


if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]  # sorted list
    target = 6  # target element to search

    obj = Solution()  # Create object of Solution class
    ind = obj.search(a, target)

    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind)

