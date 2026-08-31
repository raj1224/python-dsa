class Solution:
    # Function to merge two halves
    def merge(self, arr, low, mid, high):
        temp = []
        left, right = low, mid + 1

        # Merge both sorted halves
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # Add remaining left elements
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Add remaining right elements
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy sorted temp into original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    # Recursive merge sort
    def mergeSort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)


# Driver code
arr = [5, 2, 8, 4, 1]
sol = Solution()
sol.mergeSort(arr, 0, len(arr) - 1)
print(*arr)
