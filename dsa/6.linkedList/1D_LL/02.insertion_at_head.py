# Node class to represent each node in the linked list
class Node:
    # Constructor with data and optional next pointer
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Solution class to handle linked list operations
class Solution:
    # Function to insert a new node at the head
    def insertAtHead(self, head, newData):
        # Create a new node whose next points to current head
        newNode = Node(newData, head)
        # Return the new node as the head
        return newNode

    # Function to print the linked list
    def printList(self, head):
        temp = head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Driver code
if __name__ == "__main__":
    sol = Solution()

    # Creating a sample linked list: 2 -> 3
    head = Node(2)
    head.next = Node(3)

    print("Original List:", end=" ")
    sol.printList(head)

    # Inserting new node at head
    head = sol.insertAtHead(head, 1)

    print("After Insertion at Head:", end=" ")
    sol.printList(head)
