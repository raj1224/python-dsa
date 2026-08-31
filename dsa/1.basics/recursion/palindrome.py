# Function to check if a string is a palindrome using recursion
def palindrome(i, s):
    # Base Condition: If i exceeds half of the string, all the elements have been compared
    # and the string is a palindrome, return True.
    if i >= len(s) // 2:
        return True

    # If the start and end characters are not equal, it's not a palindrome.
    if s[i] != s[len(s) - i - 1]:
        return False

    # If both characters are the same, increment i and check start+1 and end-1.
    return palindrome(i + 1, s)

# Driver code
if __name__ == "__main__":
    s = "madam"  # Example string to check
    
    # Check if the string is a palindrome and output the result
    print(palindrome(0, s))  # Output True if palindrome, False if not
