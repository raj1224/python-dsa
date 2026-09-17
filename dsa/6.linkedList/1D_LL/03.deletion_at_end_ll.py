# Definition for singly linked list
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    # Function to delete tail node of linked list
    def deleteTail(self, head):
        # If list is empty or has one node
        if head is None or head.next is None:
            return None

        # Traverse to the second last node
        curr = head
        while curr.next.next is not None:
            curr = curr.next

        # Delete tail node
        curr.next = None

        # Return updated head
        return head

# Driver code
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

obj = Solution()
head = obj.deleteTail(head)

# Print list after deletion
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next
