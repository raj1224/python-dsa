class Solution:
    # Function to reverse digits of a number
    def reverseNumber(self, n):
        # Variable to store reversed number
        revNum = 0

        # Loop until all digits are processed
        while n > 0:
            # Get the last digit
            lastDigit = n % 10

            # Append it to the reversed number
            revNum = revNum * 10 + lastDigit

            # Remove the last digit from n
            n = n // 10

        # Return the reversed number
        return revNum

# Driver code
obj = Solution()
num = 12345
print(obj.reverseNumber(num))  # Output: 54321
