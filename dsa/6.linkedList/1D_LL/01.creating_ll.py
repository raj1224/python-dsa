# Node class represents a node in the linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data      # Data value
        self.next = next      # Pointer to next node

# Driver code
if __name__ == "__main__":
    # Create an array
    arr = [2, 5, 8, 7]

    # Create first node
    y = Node(arr[0])

    # Print memory reference of node
    print(y)

    # Print data stored in node
    print(y.data)
