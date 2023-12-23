#Print nodes at depth K
#here we are going to print depth of a node :i.e distance from the root
#we need to print all nodes at depth k
#the first base case is None we need to take care of that 
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

#it prints the depth of k ,k represents the depth how much we want to keep
def printDepthK(root,k):
    if root == None:
        return
    if k == 0:
        print(root.data)
        return 
    printDepthK(root.left, k-1)
    printDepthK(root.right, k-1)



#Approach -2 here we are mataining the current depth value i.e d and initializing it to 0 and depth value need to reach i.e k
def printDepthAtKV2(root,k,d=0):
    if root == None:
        return
    if k==d:
        print(root.data)
        return
    printDepthAtKV2(root.left,k,d+1)
    printDepthAtKV2(root.right,k,d+1)

# #this k represents the depth i.e level 0,1,2....
# print("the nodes at the given depth is ")
# printDepthK(root,2)


root = treeinput()
printTreeDetail(root)
print("Approach 2 the nodes at the given depth is ")
printDepthAtKV2(root,2)

#note:in order to print none simply give -1 and first try to finish a tree ,and then next go to other tree
