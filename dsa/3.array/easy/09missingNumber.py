def missingNum(arr):
    n = len(arr) + 1

    # Iterate from 1 to n and check
    # if the current number is present
    for i in range(1, n + 1):
        found = False
        for j in range(n - 1):
            if arr[j] == i:
                found = True
                break

        # If the current number is not present
        if not found:
            return i
    return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))