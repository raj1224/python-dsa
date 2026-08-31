class BubbleSort:
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1, -1, -1):#Iterate through the array
            did_swap = False
            for j in range(i):  #Use two nested loops to iterate over the array
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] #Swap arr[j+1] with arr[i]
                    did_swap = True
            if not did_swap:
                break

        print("After Using Bubble Sort:")
        print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before Using Bubble Sort:")
    print(" ".join(map(str, arr)))

    sorter = BubbleSort()
    sorter.bubble_sort(arr)
# 123456789101112131415161718192021222324252627282930313233343536373839
# // Define a class BubbleSort
class BubbleSort {
    
    # // Method to perform bubble sort
    bubbleSort(arr) {
        let n = arr.length;

        # // Outer loop runs from end of array towards the beginning
        for (let i = n - 1; i >= 0; i--) {
            let didSwap = false; # To check if any swapping happens in this pass

            // Inner loop compares adjacent elements
            for (let j = 0; j < i; j++) {  
                # // If current element is greater than next, swap them
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j+1]
                    let temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;

                    didSwap = true; # Mark that a swap occurred
                }
            }

            # // If no swaps happened, the array is already sorted → break early
            if (!didSwap) {
                break;
            }
        }

        # // Print the sorted array
        console.log("After Using Bubble Sort:");
        console.log(arr.join(" "));
    }
}

# // Main execution
let arr = [13, 46, 24, 52, 20, 9];
console.log("Before Using Bubble Sort:");
console.log(arr.join(" "));

# // Create object of BubbleSort class
let sorter = new BubbleSort();
sorter.bubbleSort(arr);

