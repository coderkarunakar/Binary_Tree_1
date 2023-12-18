#Print Binary Tree
#if root is leaf ,then no need to call for left and right so print its data and return  

class BinaryTreeNode:
    #Note:when ever you create a node it should have data in its constructor
    def __init__(self,data):
        self.data = data
        #initially making left ,right as None
        self.left = None
        self.right = None
        #this is for sample am not calling this printTree
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
btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(2)
btn3 = BinaryTreeNode(3)
btn4 = BinaryTreeNode(4)
btn5 = BinaryTreeNode(5)


#making btn1 left as btn2 and right as btn3
btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5
#btn1 ensures to get root from the 1 since we are considering it as a root element
#if we call btn1 it calls rest of things recursively untill it reaches leaf
printTreeDetail(btn1)
print("for print tree call")
printTree(btn1)
