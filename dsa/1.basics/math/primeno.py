# Function to check if a given number is prime
def checkPrime(n):
    cnt = 0  # Initialize a counter variable to count the number of factors

    # Loop through numbers from 1 to the square root of n
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1  # If n is divisible by i, increment the counter

            # If n is not a perfect square, count its reciprocal factor
            if n // i != i:
                cnt += 1

    # If the number of factors is exactly 2 (1 and the number itself), it's prime
    return cnt == 2

# Driver code
n = 1483  # Example number
isPrime = checkPrime(n)  # Function call to check if the number is prime

if isPrime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
