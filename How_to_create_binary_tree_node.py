#How to create Binary Tree Node
#a node will have data,and each node will have to store its children
#root will have address of its children,and these children will have address of there own children thats how we will be able reach all the nodes 
#in case of a node we want to store data,it can have upto only 2 children,in case one node has only one child ,and then child 2 will be none ,since we should have 2 childs in binary tree
#incase a node is a leaf(does not have any children) then child1,child2 both will be none
#please look notes as well for pictorial representation
#Note:A tree will never have a cycles
class BinaryTreeNode:
    #Note:when ever you create a node it should have data in its constructor
    def __init__(self,data):
        self.data = data
        #initially making left ,right as None
        self.left = None
        self.right = None
btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(4)
btn3 = BinaryTreeNode(5)

#making btn1 left as btn2 and right as btn3
btn1.left = btn2
btn1.right = btn3


        

