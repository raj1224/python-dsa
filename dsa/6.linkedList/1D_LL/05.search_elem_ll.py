# Node class for Linked List
class Node:
    def __init__(self, val):
        # Store data
        self.data = val
        # Store next pointer
        self.next = None

# Solution class containing search function
class Solution:
    # Function to search for a value in LL
    def searchValue(self, head, key):
        # Pointer to traverse the list
        current = head

        # Traverse until end
        while current is not None:
            # Check if current node matches key
            if current.data == key:
                # Return True if found
                return True
            # Move to next node
            current = current.next

        # Return False if not found
        return False

# Driver code
if __name__ == "__main__":
    # Creating linked list: 10 -> 20 -> 30
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    obj = Solution()

    # Search for value
    if obj.searchValue(head, 20):
        print("Found")
    else:
        print("Not Found")
