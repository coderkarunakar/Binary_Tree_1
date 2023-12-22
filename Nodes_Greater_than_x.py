#prints number of values greater than x

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#build tree takes a list nodes as input,represents value of nodes in  binary tree
def build_tree(nodes):
    #if input list node is empty,it returns none
    if not nodes:
        return None
#this initializes root variable as a tree node object,with the value of the first element in the nodes.list converted to an integer using int(nodes[0]),the value represents the root node of the binary tree
    root = TreeNode(int(nodes[0]))
    #creates a queue here implemented as a list,initializes with root value,the queue will be used for level order traversal to construct the tree
    queue = [root]
    # Initialize a variable i to keep track of the current index in the nodes list. Starting from index 1 because index 0 is already used for the root node.
    i = 1

    while queue:
        # Initiates a while loop that continues until the queue is empty. Within each iteration:
# node is assigned the value of the node popped from the front of the queue using queue.pop(0). This implements level-order traversa
        node = queue.pop(0)
        if i < len(nodes) and nodes[i] != -1:
            node.left = TreeNode(int(nodes[i]))
            queue.append(node.left)
        i += 1

        # Checks if there are elements left in the nodes list (i < len(nodes)) and ensures that the current node's left child exists (as -1 indicates no child). If these conditions are met and nodes[i] is not equal to -1, it creates a left child for the current node with the value int(nodes[i]) and appends this left child node to the queue
        if i < len(nodes) and nodes[i] != -1:
            node.right = TreeNode(int(nodes[i]))
            queue.append(node.right)
        i += 1
    return root

def count_nodes_greater_than_x(root, X):
    if not root:
        return 0

    count = 0
    stack = [root]
    while stack:
        #pop a node from the stack
        node = stack.pop()
        #if the value of current node node.val is greater than x then increase the count value
        if node.val > X:
            count += 1
            #check if the current node has a left child,if yes then push to stack
        if node.left:
            stack.append(node.left)
            #chekc if the current node has a right child ,if yes then push to stack
        if node.right:
            stack.append(node.right)

    return count

# Reading input
nodes = list(map(int, input().split()))
X = int(input())

# Building the binary tree
root = TreeNode(nodes)

# Counting nodes greater than X
result = count_nodes_greater_than_x(root, X)
print(result)
