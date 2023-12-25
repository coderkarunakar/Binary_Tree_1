#this is bit difficult question dry run is there in notes pls pls do look
#pls look class notes to understand input and output its all about Left,Root ,Right starts from down to up it was build ,   
#Binary tree creation,Tree node class,update node value with class,inorder traversal(updating node value to a list),main function (replaceNodeWithDepth),finally execution

#Replace Node with Depth
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        #we can find depth with the help of this below function
def updateTreeDepth(root,depth):
    #base case if no root then simply return nothing
    if not root:
        return
        #root points to depth
    root.val =depth
    #updates left and right  subtree with an increment depth
    updateTreeDepth(root.left,depth+1)
    updateTreeDepth(root.right,depth+1)
#inorder traversal

def inorderTraversal(root,result):
    #base case returns none if no root is there
    if not root:
        return
        #it travels in left,root,right manner..
    inorderTraversal(root.left,result)
#appends the current node valto the result
    result.append(root.val)
    inorderTraversal(root.right,result)

def replacenodewithDepth(nodes):
    if not nodes:
        return
        # Creates the root node of the binary tree using the first element of the nodes list.
    root = TreeNode(int(nodes[0]))
    # Initializes a queue with the root node.
    queue = [root]
    #traversing the queue,and poping the values from it
    i = 1
    #Tree Construction using Queue,this runs untill the queue is empty
    while queue:
#Dequeues the first node from the queue for the processing
        current = queue.pop(0)
       #checks if the next element in the node list is not equal to -1
       #left iteration
        if nodes[i]!= -1:
            #creates a left child
            current.left = TreeNode(int(nodes[i]))
            #enqueues the newly created left child node into queue further processing
            queue.append(current.left)
            #to move to the next element in the queue
        i+=1
        #right iteration
        if nodes[i]!= -1:
            current.right = TreeNode(int(nodes[i]))
            queue.append(current.right)
        i +=1
    #update the tree with depth 
    #updating the node value of the tree with their respective depths starting from 0
    updateTreeDepth(root, 0)
    #initialize empty list to store the inorder traversal result
    result = []
    #performs inorder traversal,and appends the node value(depths) to the results list
    inorderTraversal(root,result)
    #prints the space seperated node value(depths) after converting them to strings
    print(' '.join(map(str, result)))

    
nodes = list(map(int, input("enter nodes").split()))
replacenodewithDepth(nodes)

   


    

    


        




        
     


        