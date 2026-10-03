from typing import List
# To understand the concept please dry run the code on arr = [4, 3, 1, 5, 2]
# Only way to understand Quick Sort is using dry-run!


class Solution:
    def quickSort(self, arr: List[int], low: int, high: int) -> None:
        if low < high:
            pi = self.partition(arr, low, high)

            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)

    def partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[low]  # consider the first element as the pivot element
        i, j = low, high

        while i < j:
            while i < high and arr[i] <= pivot:
                i += 1
            while j > low and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]

        return j
