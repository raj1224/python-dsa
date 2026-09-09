class ArrayManipulator:
    def rearrange_by_sign(self, A):
        n = len(A)
        ans = [0] * n  # Initialize result array with zeros

        pos_index = 0  # Even indices for positive numbers
        neg_index = 1  # Odd indices for negative numbers

        for i in range(n):
            if A[i] < 0:
                # Place negative at odd index
                ans[neg_index] = A[i]
                neg_index += 2
            else:
                # Place positive at even index
                ans[pos_index] = A[i]
                pos_index += 2

        return ans

# Main execution
if __name__ == "__main__":
    A = [1, 2, -4, -5]
    obj = ArrayManipulator()
    result = obj.rearrange_by_sign(A)
    print(" ".join(map(str, result)))
