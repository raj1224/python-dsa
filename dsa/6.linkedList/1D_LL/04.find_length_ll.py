# Node class to represent each element in the linked list
class Node:
    # Constructor to initialize data and next pointer
    def __init__(self, data1):
        self.data = data1
        self.next = None

# Solution class containing the method to find length
class Solution:
    # Function to find the length of the linked list
    def lengthOfLinkedList(self, head):
        # Initialize counter to 0
        count = 0

        # Initialize a temporary pointer to head
        temp = head

        # Traverse the linked list
        while temp is not None:
            # Increment count for each node
            count += 1

            # Move to the next node
            temp = temp.next

        # Return the total count
        return count

# Driver code
if __name__ == "__main__":
    # Creating a sample linked list
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    # Create Solution object
    obj = Solution()

    # Find and print the length of linked list
    print("Length of Linked List:",
          obj.lengthOfLinkedList(head))
