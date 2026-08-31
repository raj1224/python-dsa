class Solution:
    # Recursive function to find sum of first N natural numbers
    def sumOfNaturalNumbers(self, N):
        # Base case: if N is 1, return 1
        if N == 1:
            return 1
        # Recursive case: current number + sum of previous numbers
        return N + self.sumOfNaturalNumbers(N - 1)

# Driver code
if __name__ == "__main__":
    obj = Solution()
    N = int(input())
    print(obj.sumOfNaturalNumbers(N))
