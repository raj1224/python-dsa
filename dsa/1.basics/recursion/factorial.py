# Recursive approach
# Recursive function to calculate factorial of a number
def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1

    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)

# Define the number to compute factorial
n = 3

# Call the factorial function and print the result
print(factorial(n))

# Iterative approach

# Function to calculate factorial of a number
def factorial(X):
    ans = 1

    # Loop from 1 to X to compute factorial
    for i in range(1, X + 1):
        ans *= i

    # Return the final result
    return ans

# Input value for which factorial is to be calculated
X = 5

# Call the factorial function and store the result
result = factorial(X)

# Print the result
print(f"The factorial of {X} is {result}")
