from turtle import right
from a1_partc import Queue

INORDER = 1
PREORDER = 2
POSTORDER = 3
BREADTHFIRST = 4
REVERSE = 5

class BST:
    class Node:
        def __init__(self,data,left=None,right=None):
            self.data=data 
            self.left=left
            self.right=right
    def __init__(self):
        self.root=None 
    def ins(self,subtree,value):
        if subtree is None:
            return BST.Node(value)
        if value <subtree.data:
            if subtree.left is None:
                subtree.left=BST.Node(value)
            else:
                subtree.left=self.ins(subtree.left,value)
        else:
            if subtree.right is None:
                subtree.right=BST.Node(value)
            else: 
                subtree.right=self.ins(subtree.right,value)
        return subtree
    def insertRecursive(self,value):
        self.root=self.ins(self.root,value)
    def printInorder(self,subtree):
        if subtree is not None:
            self.printInorder(subtree.left)
            print(subtree.data)
            self.printInorder(subtree.right)
    def printReverse(self,subtree):
        if subtree is not None:
            self.printReverse(subtree.right)
            print(subtree.data)
            self.printReverse(subtree.left)
    def printPreorder(self,subtree):
        if subtree is not None:
            print(subtree.data)
            self.printPreorder(subtree.left)
            self.printPreorder(subtree.right)
    def Breadthfirst(self):
        q=Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            curr=q.dequeue()
            if curr :
                print(curr.data)
                if curr.left:
                    curr.left=q.enqueue(curr.left)
                if curr.right:
                    curr.right=q.enqueue(curr.right)
        
        


    def print(self, mode=INORDER):
        if mode == INORDER:
            self.printInorder(self.root)
        elif mode == REVERSE:
            self.printReverse(self.root)
        elif mode == PREORDER:
            self.printPreorder(self.root)
        elif mode == BREADTHFIRST:
            self.Breadthfirst()

# Testing the corrected implementation
tree = BST()
tree.insertRecursive(20)
tree.insertRecursive(10)
tree.insertRecursive(25)
tree.insertRecursive(5)
tree.insertRecursive(15)
tree.insertRecursive(35)
tree.insertRecursive(30)
tree.insertRecursive(40)

tree.print(PREORDER)
