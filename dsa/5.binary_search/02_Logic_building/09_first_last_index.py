# USING UPPER AND LOWER BOUND
from typing import List

class Solution:
    """
    Counts how many times the target appears
    in the sorted array.
    """
    def count_occurrence(self, arr: List[int], target: int) -> int:
        # Store the total number of matches found so far.
        count: int = 0

        # Check every element in the array.
        for value in arr:
            # Increase the answer when the current value matches the target.
            if value == target:
                count += 1

        return count


# Driver code starts
def main() -> None:
    arr: List[int] = [1, 1, 2, 2, 2, 2, 3]
    target: int = 2

    obj = Solution()
    print(obj.count_occurrence(arr, target))


if __name__ == "__main__":
    main()



# USING BINARY SEARCH

from typing import List

class Solution:
    """
    Counts how many times the target appears
    in the sorted array.
    """
    def count_occurrence(self, arr: List[int], target: int) -> int:
        # Find the first position where value is at least target.
        first: int = self.lower_bound(arr, target)

        # If target is absent, there is nothing to count.
        if first == len(arr) or arr[first] != target:
            return 0

        # Find the first position where value becomes greater than target.
        after_last: int = self.upper_bound(arr, target)

        return after_last - first

    def lower_bound(self, arr: List[int], target: int) -> int:
        low: int = 0
        high: int = len(arr) - 1

        # Keep the best lower bound found so far.
        answer: int = len(arr)

        while low <= high:
            mid: int = low + (high - low) // 2

            # This index can be a lower bound, so remember it and move left.
            if arr[mid] >= target:
                answer = mid
                high = mid - 1
            else:
                # Current value is too small, so move to the right side.
                low = mid + 1

        return answer

    def upper_bound(self, arr: List[int], target: int) -> int:
        low: int = 0
        high: int = len(arr) - 1

        # Keep the best upper bound found so far.
        answer: int = len(arr)

        while low <= high:
            mid: int = low + (high - low) // 2

            # This index is greater than target, so it can be an upper bound.
            if arr[mid] > target:
                answer = mid
                high = mid - 1
            else:
                # Current value still belongs to target or lies before it.
                low = mid + 1

        return answer


# Driver code starts
def main() -> None:
    arr: List[int] = [1, 1, 2, 2, 2, 2, 3]
    target: int = 2

    obj = Solution()
    print(obj.count_occurrence(arr, target))


if __name__ == "__main__":
    main()