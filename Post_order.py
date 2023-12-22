#steps:Tree building->check nodes is empty using len 
                    # ->assign node value into root and assing into queue and travel through it
                    #pop the last value 
                    #create a condition still more nodes are present in the index and index should not equal to -1 create a left node and right node
                    #finall return the root
        #post order:check root is empty ,and return empty list
        #create a result list,stack list ,and append the root values into the stack ,remove each element and append it to the result
        #append the left value nd right values into the stack and fianlly reverse the list in order to obtain the post order and finally retun it and call all the methods



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#creating a function with parameter nodes
def build_tree(nodes):
    #if nodes are empty simply return none since there is no elements
    if len(nodes) == 0:
        return None
#initialing index as 0 and iterating it,
    index = 0
    #creating a root node of the binary tree using the first element of the nodes list.
    #it assumes that nodes are represented as strings so it is converted into the int
    #type Node is assumed to be else where in the code,and increasing the value of index,untill all nodes get completed
    root = Node(int(nodes[index]))
    index += 1
#initialing queue ds with the root node
    queue = [root]
    #loop runs untill queue get completed
    while queue:
        #dequeues the first element from the queue
        current = queue.pop(0)
# checks if more nodes are there in the index and ensures index should not equal to -1 i.e null
        if index < len(nodes) and nodes[index] != -1:
#if the condition is met then it creates a left child 
            current.left=Node(int(nodes[index]))
            #finally appends to the queue 
            queue.append(current.left)
            #increasing value to iterate
        index += 1
#same process as above but here creates a right node and append it to the queue
        if index < len(nodes) and nodes[index] != '-1':
            current.right = Node(int(nodes[index]))
            queue.append(current.right)
        index += 1
#finally returns the root
    return root

#it takes the root node of  the binary tree as an argument
def post_order(root):
    #checks if root node is empty then returns an empty array(list)
    if root is None:
        return []

    result = []
    stack = []
    stack.append(root)
#traveling through the root values of stack 
    while stack:
        #removing elements from stack and assigning a value as current
        current = stack.pop()
        #appending to result
        result.append(current.data)
#appending the left and right values into the stack
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
#this revereses the list to obtain post order sequence (right ,left,root)
    return result[::-1]

# Reading input
nodes = input().strip().split()

# Building the binary tree
root = build_tree(nodes)

# Performing post-order traversal and printing the result
result = post_order(root)
print(' '.join(map(str, result)))







