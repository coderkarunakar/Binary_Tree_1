class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Building a tree
def buildTree(arr):
    #checking wheather arr is empty or array starting index is -1 then return None
    if not arr or arr[0] == -1:
        return None
    
    #assigning starting index of array is 0
    root = Node(arr[0])
    #assigning it to stack variable
    stack = [root]
    #initializing i and running loop till stack
    i = 1
    while stack:
        #removing all elements from stack which was assigned previously
        curr_node = stack.pop()
        #checking condition arr index should not be equal to -1 and assigning to left node and again appending to empty stack 
        if arr[i] != -1:
            curr_node.left = Node(arr[i])
            stack.append(curr_node.left)
        #increasing i value to iterate to next level
        i += 1
        #same process for right values as well
        if arr[i] != -1:
            curr_node.right = Node(arr[i])
            stack.append(curr_node.right)
        
        i += 1
    
    return root

# this is for printing purpose
def preOrderTraversal(root):
    if root is None:
        return
    
    print(root.data, end=" ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

# Reading input
nodes = list(map(int, input().split()))

# Building the tree
root = buildTree(nodes)

# Perform pre-order traversal and print the result
preOrderTraversal(root)
