

from a1_partc import Queue

INORDER = 1
PREORDER = 2
POSTORDER = 3
BREADTHFIRST = 4
REVERSE = 5

# remember recursive must return subtree
# print => Inorder, Preorder -left,data,right , 
#          Reverse => right , data, left
#          Breadthfirst : 
# class BST:
#     class Node:
#         def __init__(self,data,left=None,right=None):
#             self.data=data 
#             self.left=left
#             self.right=right
            
#     def __init__(self):
#         self.root=None 
        
#     def ins(self,subtree,value):
#         if subtree is None:
#             return BST.Node(value)
#         if value <subtree.data:
#             if subtree.left is None:
#                 subtree.left=BST.Node(value)
#             else:
#                 subtree.left=self.ins(subtree.left,value)
#         else:
#             if subtree.right is None:
#                 subtree.right=BST.Node(value)
#             else: 
#                 subtree.right=self.ins(subtree.right,value)
#         return subtree # chu y
    
#     def insertRecursive(self,value):
#         self.root=self.ins(self.root,value)
    
#     def removeR(self, value):
#         self.root = self.remove(self.root, value)  
       
#     def remove(self,node, value):
#         if node is None:
#             return None  # Value not found

#         if value < node.data:
#             node.left = self.remove(node.left, value)
#             return node
#         elif value > node.data:
#             node.right = self.remove(node.right, value)
#             return node
#         else:  # Found the node to remove
#             if node.left is None and node.right is None:  # Leaf node
#                 return None
#             elif node.left is None:  # Only right child
#                 return node.right
#             elif node.right is None:  # Only left child
#                 return node.left
#             else:  # Two children
#                 # Find inorder successor (smallest node in right subtree)
#                 successor = node.right
#                 while successor.left is not None:
#                     successor = successor.left
#                 # Replace node's data with successor's data
#                 node.data = successor.data
#                 # Remove successor from right subtree
#                 node.right = self.remove(node.right, successor.data)
#                 return node

#     # Inorder traversals: 
#     #  visit its left subtree
#     #  visit a node
#     #  visit its right subtree

    # def printInorder(self,subtree):
    #     if subtree !=None:
    #         self.printInorder(subtree.left)
    #         print(subtree.data)
    #         self.printInorder(subtree.right)
     
#     def printReverse(self,subtree):
#         if subtree !=None:
#             self.printReverse(subtree.right)
#             print(subtree.data)
#             self.printReverse(subtree.left)
           
#     # Preorder traversals 
#     # visit a node
#     # visit its left subtree
#     # visit its right subtree
#     def printPreorder(self,subtree):
#         if subtree != None:
#             print(subtree.data)
#             self.printPreorder(subtree.left)
#             self.printPreorder(subtree.right)
           
#     # Postorder traversals: 
#         #   visit its left subtree
#         #   visit its right subtree
#         #   visit a node  
#     def printPostorder(self,subtree):
#         if subtree is not None:
#             self.printPostorder(subtree.left)
#             self.printPostorder(subtree.right)
#             print(subtree.data)
           
#     def printBreadthFirst(self):
#         q=Queue()
#         q.enqueue(self.root)
#         while not q.is_empty():
#             curr=q.dequeue()
#             if curr :
#                 print(curr.data)
#                 if curr.left:
#                     curr.left=q.enqueue(curr.left)
#                 if curr.right:
#                     curr.right=q.enqueue(curr.right)  
class BST:
    class Node():
        def __init__(self,data,left=None,right=None):
            self.data=data 
            self.left=left 
            self.right=right 
    def __init__(self):
        self.root=None 
    def ins(self,subtree,value):
        if subtree is None:
            return BST.Node(value)
        else:
            if value<subtree.data:
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
    def search(self,subtree,value):
        if subtree is None:
            return False
        else:
            if subtree.data== value:
                return True
            elif value <subtree.data:
                subtree.left=self.search(subtree.left,value)
            elif value > subtree.data:
                subtree.right=self.search(subtree.right,value)
        return False
    
    def searchR(self,value):
        self.root=self.search(self.root,value)

    def removeR(self,value):
        self.root=self.remove(self.root,value)
    def remove(self,node,value):
        if node is None:
            return None
        if value <node.data:
            node.left=self.remove(node.left,value)
            return node 
        elif value >node.data:
            node.right=self.remove(node.right,value)
            return node 
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                su=node.right
                while su.left is not None:
                    su=su.left
                node.data=su.data
                node.right=self.remove(node.right,su.data)
                return node

    def printInorder(self,subtree):
        if subtree !=None:
            self.printInorder(subtree.left)
            print(subtree.data)
            self.printInorder(subtree.right)




    def print(self,mode=INORDER):
        if mode== INORDER:
            self.printInorder(self.root)
        elif mode==REVERSE:
            self.printReverse(self.root)
        elif mode==PREORDER:
            self.printPreorder(self.root)
        elif mode==POSTORDER:
            self.printPostorder(self.root)
        elif mode==BREADTHFIRST:
            self.printBreadthFirst()  
  
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

tree.print(INORDER)
print('---------------------------------')
tree.removeR(40)
tree.print(INORDER)