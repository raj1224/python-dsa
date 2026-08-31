# Function to check if a given integer is a palindrome
def palindrome(n):
    revNum = 0  # Initialize a variable to store the reverse of the number
    dup = n  # Create a duplicate variable to store the original number

    # Iterate through each digit of the number until it becomes 0
    while n > 0:
        ld = n % 10  # Extract the last digit of the number
        revNum = (revNum * 10) + ld  # Build the reverse number by appending the last digit
        n //= 10  # Remove the last digit from the original number

    # Check if the original number is equal to its reverse
    return dup == revNum  # Return True if they are equal, otherwise False

# Driver code
number = 4554  # Example number
if palindrome(number):  # Check if the number is a palindrome
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
