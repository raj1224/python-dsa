# forward recursion
class Solution:
    # Recursive function to print numbers from current to n
    def printNumbers(self, current, n):
        # Base case: if current exceeds n, stop recursion
        if current > n:
            return

        # Print current number
        print(current, end=' ')

        # Recursive call with next number
        self.printNumbers(current + 1, n)


if __name__ == "__main__":
    sol = Solution()
    n = 10

    sol.printNumbers(1, n)
    print()

class Solution:
    # Recursive function to print numbers from current to n using backtracking
    def printNumbers(self, current, n):
        # Base case: if current exceeds n, stop recursion
        if current > n:
            return

        # Recursive call with next number
        self.printNumbers(current + 1, n)

        # Print current number during backtracking
        print(current, end=' ')


if __name__ == "__main__":
    sol = Solution()
    n = 10

    sol.printNumbers(1, n)
    print()
