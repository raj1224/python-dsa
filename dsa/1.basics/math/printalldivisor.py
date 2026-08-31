import math

class Solution:
    # Function to get all divisors
    def getDivisors(self, N):
        # Create list to store divisors
        res = []

        # Loop from 1 to square root of N
        for i in range(1, int(math.isqrt(N)) + 1):
            # Check if i divides N
            if N % i == 0:
                # Add i to result
                res.append(i)

                # If N // i is not the same, add that too
                if i != N // i:
                    res.append(N // i)

        # Return the list of divisors
        return res

# Create object of Solution class
sol = Solution()

# Input number
N = 36

# Get divisors
result = sol.getDivisors(N)

# Print the result
print("Divisors of", N, ":", *result)
