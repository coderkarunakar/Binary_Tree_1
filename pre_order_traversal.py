class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(arr):
    if not arr or arr[0] == -1:
        return None
    
    root = Node(arr[0])
    stack = [root]
    i = 1
    while stack:
        curr_node = stack.pop()
        
        if arr[i] != -1:
            curr_node.left = Node(arr[i])
            stack.append(curr_node.left)
        
        i += 1
        
        if arr[i] != -1:
            curr_node.right = Node(arr[i])
            stack.append(curr_node.right)
        
        i += 1
    
    return root

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
