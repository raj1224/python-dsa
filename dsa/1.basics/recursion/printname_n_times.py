class Solution:
    # Recursive function to print name count times
    def printName(self, name, count, N):
        # Base case: if count equals N, stop recursion
        if count == N:
            return

        # Print the name
        print(name)

        # Recursive call with incremented count
        self.printName(name, count + 1, N)

if __name__ == "__main__":
    sol = Solution()
    N = 5
    name = "Ashish"

    sol.printName(name, 0, N)
