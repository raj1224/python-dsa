# BETTER APPROACH
def main():
    n = 5

    # If n is 0, only the first term is printed
    if n == 0:
        print(f"The Fibonacci Series up to {n}th term:")
        print(0)
    else:
        second_last = 0  # (i-2)th term
        last = 1         # (i-1)th term

        print(f"The Fibonacci Series up to {n}th term:")
        print(f"{second_last} {last}", end=" ")

        for i in range(2, n + 1):
            cur = last + second_last  # Current ith Fibonacci number
            second_last = last        # Move window
            last = cur
            print(cur, end=" ")

if __name__ == "__main__":
    main()

# OPTIMAL APPROACH
def fibonacci(N):
    # Base case: if N is 0 or 1, return N
    if N <= 1:
        return N

    # Recursive calls: calculate previous two terms
    last = fibonacci(N - 1)   # (N-1)th term
    slast = fibonacci(N - 2)  # (N-2)th term

    return last + slast

# Driver code
N = 4
print(fibonacci(N))  # Output: 3
    