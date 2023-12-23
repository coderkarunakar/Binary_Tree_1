#No of leaf Nodes:
#input of a binary tree
class BinaryTreeNode:
    #Note:when ever you create a node it should have data in its constructor
    def __init__(self,data):
        self.data = data
        #initially making left ,right as None
        self.left = None
        self.right = None
def printTree(root):
    if root == None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)
def printTreeDetail(root):
    #works untill leaf node i.e which has no child ,this is the base case of recursive call
    if root == None:
        return
    print(root.data, end=':')
    if root.left != None:
        print("L", root.left.data, end=',')
    if root.right != None:
        print("R", root.right.data, end=' ')
        #this is to get into a new line
    print()
    printTreeDetail(root.left)
    printTreeDetail(root.right)

#its going to ask user to give input,and it returns the root of the tree
#smaller tree input we will get through recursively
def treeinput():
    rootData = int(input("enter"))
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    #calling above method in order to get repeat above steps
    leftTree = treeinput()
    rightTree = treeinput()
    #just assigning it
    root.left = leftTree
    root.right = rightTree
    return root

#Counting no of leaf nodes for a Tree
def numleafNodes(root):
    #if the root is none simply return zero (0),,for an empty tree there are no leaf nodes  ,like if we have 1 leaf node at left and no leaf node at right or vice versa also this works
    if root == None:
        return 0

    #if both the roots are None then simply return 1,since in this case root it self is an leaf node so we are returning 1,if we have left or right leaf node that else case works
    if root.left == None and root.right == None:
        return 1
    numLeafLeft = numleafNodes(root.left)
    numLeafRight = numleafNodes(root.right)
    return numLeafLeft + numLeafRight
root = treeinput()
printTreeDetail(root)
print("the no of leaf nodes are ",numleafNodes(root))


#note:in order to print none simply give -1 and first try to finish a tree ,and then next go to other tree

