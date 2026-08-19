class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def insert(self, value):
        if (root != None):
            return Node(value)
        if(root.data == value):
            return root
        if(root.data > value):
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root

def search(root,value):
    if(root == None):
        print("Element not found",end="\n")
        return
    if(root.data == value):
        print("Element found",end="\n")
        return
    if(root.data > value):
        search(root.left,value)
    else:
        search(root.right,value)

def get_successor(root):
    root = root.right
    while(root != None and root.left != None):
        root = root.left
    return root

# DELETION IN BST
def delete(root,value):
    if(root == None):
        return root
    if(root.data > value):
        delete(root.left, value)
    if(root.data < value):
        delete(root.right, value)
    else:
        if(root.left == None):
            return root.right
        if(root.right == None):
            return root.left
        else:
            succ = get_successor(root)
            root.data = succ.data
            root.right = delete(root.right, succ.data)
    return root
        

def InOrder(root):
    if (root != None):
        InOrder(root.left)
        print(root.data, end = " ")
        InOrder(root.right)

root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 25)
root = insert(root, 2)
root = insert(root, 18)

InOrder(root)