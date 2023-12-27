#Doubt problem pls take a look

#Nodes with out sibling
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Function to print nodes without siblings
def printNodesWithoutSibling(root):
    if root is None:
        return
    
    if root.left is not None and root.right is None:
        print(root.left.val, end=' ')
    
    if root.right is not None and root.left is None:
        print(root.right.val, end=' ')
    
    printNodesWithoutSibling(root.left)
    printNodesWithoutSibling(root.right)

# Build the tree from given input
def buildTree(nodes):
    if not nodes:
        return None
    
    index = 0
    root = TreeNode(int(nodes[index]))
    index += 1

    queue = [root]
    while queue:
        current = queue.pop(0)

        if index < len(nodes) and nodes[index] != '-1':
            current.left = TreeNode(int(nodes[index]))
            queue.append(current.left)
        index += 1

        if index < len(nodes) and nodes[index] != '-1':
            current.right = TreeNode(int(nodes[index]))
            queue.append(current.right)
        index += 1

    return root

# Reading input
nodes_input = input().split()

# Building the tree
root_node = buildTree(nodes_input)

# Printing nodes without siblings
printNodesWithoutSibling(root_node)
