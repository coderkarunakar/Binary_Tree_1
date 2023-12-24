#Doubt and take a look pls dry run it 

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
    root = TreeNode(int(nodes[0]))
    queue = [root]
    #traversing the queue,and poping the values from it
    i = 1
    while queue:
        #poping the last value from the queue
        current = queue.pop(0)
        #if the node value is not equal to -1 then pick the left value and append it to queue,same for right as well
        if nodes[i]!= -1:
            current.left = TreeNode(int(nodes[i]))
            queue.append(current.left)
        i+=1
        if nodes[i]!= -1:
            current.right = TreeNode(int(nodes[i]))
            queue.append(current.right)
        i +=1
    #update the tree with depth 
    updateTreeDepth(root, 0)
    #perform in order traversal to print modified tree
    result = []
    inorderTraversal(root,result)
    print(' '.join(map(str, result)))

    
nodes = list(map(int, input("enter nodes").split()))
replacenodewithDepth(nodes)

   


    

    


        

        
     


        