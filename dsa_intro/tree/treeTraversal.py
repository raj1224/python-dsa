class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

def preorder(root):
    if (root != None):
        print(root.data, end = " ")
        preorder(root.left)
        preorder(root.right)

def InOrder(root):
    if (root != None):
        InOrder(root.left)
        print(root.data, end = " ")
        InOrder(root.right)

def postorder(root):
    if (root != None):
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = " ")

root=Node(1)
root.left=Node(2)
root.right=Node(3)