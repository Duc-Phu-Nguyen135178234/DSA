
        
# Hash table (key,value)
# insert chain -> key , value 
# heap insert -> data -> check
# AVL -> node (*** no parent only height) , balance , updateheight , insert(subtree,data)
  
        # self.updateheight(subroot)  ########## update subroot
        # balance_num=self.balance(subroot)

# Red -> parent,insertRecursive(curr,new_node), insert(self,data)-> make new_node rightaway
#  remember need recursive(curr,new_node) and insert function check self root is None first.
# fix function 

        

#HASH TABLE Closing Address
from itertools import filterfalse
#key value for hash table
# insert if 
# remove dau . curr.pre=None => self.table[idx]=curr.next=>curr.next:curr.next.pre=None

class hashtable():
    class Node():
        def __init__(self,key,value,next=None,pre=None):
            self.key = key
            self.value = value
            self.next = None  
            self.pre=None
            
    def __init__(self,cap):
        self.cap=cap 
        self.table=[None]* cap 
    def hash_function(self,key):
        return hash(key)%self.cap
    
    def insert(self,key,value):
        idx=self.hash_function(key)
        curr=self.table[idx]
        if self.table[idx] is None:
            self.table[idx]=self.Node(key,value)
        else:
            while curr: ## chu y 
                curr=curr.next
            new_node=self.Node(key,value)
            curr.next=new_node 
            new_node.next=None 
    def remove(self,key,value):
        idx=self.hash_function(key)
        curr=self.table[idx]
        while curr:
            if curr.key==key:
                if curr.pre is None:
                    self.table[idx]=curr.next 
                    if curr.next : ####chu y 
                        curr.next.pre=None
                elif curr.next is None:###
                    curr.pre.next=None #### Chu Y luon luon kg nho 
                else:
                    pre_node=curr.pre
                    next_node=curr.next
                    pre_node.next=next_node
                    next_node.pre=pre_node 
                return True
            else:
                curr=curr.next  
        return False 
    def search(self,key):
        idx=self.hash_function(key)
        curr=self.table[idx]
        while curr:
            if curr.key==key:
                return True 
            else:
                curr=curr.next
        return False
        
class LinearProbingHashTable:
    def __init__(self,key,value,cap=10):
        self.key=key 
        self.value=value 
        self.cap=cap 
        self.table=[None] % self.cap 
    def hash_function(self,key):
        return hash(key)%self.cap 
    def insert(self,key,value):
        idx=self.hash_function(key)
        orginal=idx
        while self.table[idx] is not None:
            if self.table[idx][0]==key:
                self.table[idx]=(key,value)
            idx=(idx+1)%self.cap
            if orginal==idx:
                raise IndexError('full')
        self.table[idx]=(key,value) 
    def search(self,key):
        idx=self.hash_function(key) 
        orginal=idx 
        while self.table[idx] is not None:
            if self.table[idx][0]==key:
                return True 
            idx=(idx+1)%self.cap
            if orginal==idx:
                return False 
        return False 
    def remove(self,key):
        idx=self.hash_function(key)
        orginal=idx
        while self.table[idx] is not None:
            if self.table[idx][0]==key:
                self.table[idx]=None
                empty_idx=idx
                break
            idx=(idx+1)%self.cap
            if orginal==idx:
                return False
            
        curr=(empty_idx+1)%self.cap 
        while self.table[curr] is not None:
            curr_key,curr_value=self.table[curr]
            properhash=self.hash_function(curr_key)
            if properhash<empty_idx<curr:
                self.table[empty_idx]=curr_key,curr_value
                self.table[curr]=None
                empty_inx=curr
            curr=(empty_idx+1)%self.cap

 

#HASH TABLE Opening Address
# array : self.table.self.tombstone,key,value
#chu y insert check lien if .
    #search and remove while curr is mot None
class Tombstone():
    def __init__(self,key,value,cap=10):
        self.key=key 
        self.value=value
        self.cap=cap 
        self.table=[None] *self.cap 
        self.tombstone="tombstone"
        
    def hash_function(self,key):
        return hash(key)%self.cap
    
    def insert(self,key,value):
        index=self.hash_function(key)
        orginal_index=index 
        if self.table[index] is None or self.table[index]==self.tombstone:
            self.table[index]=(key,value)
        else:
            while self.table[index] is not None and self.table[index]!=self.tombstone: # chu y
                index=(index+1)%self.cap
                if index==orginal_index:
                    raise IndexError('Full table')
            self.table[index]=(key,value) 
            
    def search(self,key):
        index=self.hash_function(key)
        orginal_index=index 
        while self.table[index] is not None: # chu y while dau tien
            if self.table[index][0]==key and self.table[index]!=self.tombstone:
                return True # chu y [0]
            index=(index+1)%self.cap
            if index==orginal_index:
                return False
        return False 
    
    def remove(self,key):
        index= self.hash_function(key)
        orginal_index=index 
        while self.table[index] is not None:
            if self.table[index][0]==key and self.table[index]!=self.tombstone:
                self.table[index]=None
                self.table[index]=self.tombstone
            index=(index+1)%self.cap 
            if index==orginal_index:
                return False

#HEAP Min_heap and Max_Heap
# check _value(idx)whileidx>0 
# parent=(idx-1)//2 diff (n//2)-1
class Heap():
    def __init__(self):
        self.heap=[] 
    def insert(self,data):
        self.heap.append(data)
        self.check_value(len(self.heap)-1)
    def check_value(self,idx):
        while idx >0:  ## chu y
            parent=(idx-1)//2 #chu y
            if self.heap[idx] < self.heap[parent]:
                self.heap[idx],self.heap[parent]=self.heap[parent],self.heap[idx]
                idx=parent 
            else: break #chu y
    def min_heap(self,idx):
        n=len(self.heap)
        smallest=idx
        left_child=2*idx+1 
        right_child=2*idx+2
        
        if left_child < n and self.heap[left_child] < self.heap[smallest]:
            smallest=left_child 
        if right_child < n and self.heap[right_child] < self.heap[smallest]:
            smallest=right_child
        if smallest != idx :
            self.heap[smallest],self.heap[idx]=self.heap[idx],self.heap[smallest]
            self.min_heap(smallest)
    def remove(self):
        if len(self.heap)==0:
            return 0
        if len(self.heap)==1:
            return self.heap.pop()
        min_value=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.min_heap(0)
        return min_value # chu y
    def max_heap(self,idx):
        n=len(self.heap)
        largest=idx
        left_child=2*idx+1
        right_child =2*idx+2 
        if left_child<n and self.heap[left_child] > self.heap[largest]:
            largest=left_child
        if right_child<n and self.heap[right_child] > self.heap[largest]:
            largest=right_child 
        if largest !=idx:
            self.heap[largest],self.heap[idx]=self.heap[idx],self.heap[largest] 
            self.max_heap(largest)
    def sort(self):
        n=len(self.heap)
        
        for i in range((n//2)-1,-1,-1):
            self.max_heap[i] 
        for i in range(n-1,0,-1):
            self.heap[i],self.heap[0]=self.heap[0],self.heap[i]
            self.max_heap(0) # chu y

# AVL TREE => using node and height to balance tree
# balance and updateheight no loop 
# insert(subroot,new_node)
class AVL():
    class Node():
        def __init__(self,data,left=None,right=None):
            self.data=data 
            self.left=left 
            self.right=right 
            self.height=1 
    def __init__(self):
        self.root=None 
    def balance(self,node):
        if node is None:
            return 0
        leftheight= node.left.height if node.left else 0 
        rightheight= node.right.height if node.right else 0
        return rightheight -leftheight 
    def updateheight(self,node):
        if node is not None:
            leftheight= node.left.height if node.left else 0
            rightheight = node.right.height if node.right else 0
            node.height=1+max(leftheight,rightheight)
    def insert(self,subroot,data):
        if subroot is None:
            return self.Node(data) # chu Y
        
        if data<subroot.data:
            subroot.left=self.insert(subroot.left,data)
        else:
            subroot.right=self.insert(subroot.right,data)
        
        self.updateheight(subroot)  ########## update subroot
        balance_num=self.balance(subroot)
        if balance_num ==2 :
            if self.balance(subroot.right)==-1: # chu y self.balance
                subroot.right = self.rightRotate(subroot.right)
            subroot=self.leftRotate(subroot)
        if balance_num==-2:
            if self.balance(subroot.left)==1:
               subroot.left= self.leftRotate(subroot.left)
            subroot=self.rightRotate(subroot)
        return subroot # chu y
    def rightRotate(self,A):
        B=A.left 
        A.left=B.right
        B.right=A 
        self.updateheight(A)
        self.updateheight(B)
        return B
    def leftRotate(self,A):
        B=A.right
        A.right=B.left
        B.left=A
        self.updateheight(A) 
        self.updateheight(B)
        return B



#
class RedBlackTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.color = 'RED'  
            self.left = None
            self.right = None
            self.parent = None
    def __init__(self):
        self.root = None  

    def insert(self, data):
        new_node = self.Node(data)
        if self.root is None:
            self.root = new_node
            self.root.color = 'BLACK' 
        else:
            self.insert(self.root, new_node)
            self.fix_insert(new_node)

    def insertR(self, current, new_node):
       
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
                new_node.parent = current ## Chu Y
            else: 
                self.insertR(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
                new_node.parent = current
            else:
                self.insertR(current.right, new_node)

    def fix_insert(self, C):
        
        while C != self.root and C.parent.color == 'RED': ## chu Y
            P = C.parent
            G = P.parent

            if P == G.left: 
                S = G.right  
                if S and S.color == 'RED':  
                    P.color = 'BLACK'
                    S.color = 'BLACK'
                    G.color = 'RED'
                    C = G
                else:
                    if C == P.right: ## chu y S same 
                        C = P
                        self.left_rotate(C)
                    P.color = 'BLACK'  
                    G.color = 'RED'
                    self.right_rotate(G)
            else:  
                S = G.left  
                if S and S.color == 'RED': 
                    P.color = 'BLACK'
                    S.color = 'BLACK'
                    G.color = 'RED'
                    C = G
                else:
                    if C == P.left:  
                        C = P
                        self.right_rotate(C)
                    P.color = 'BLACK'  
                    G.color = 'RED'
                    self.left_rotate(G)

        self.root.color = 'BLACK' # chu y



    # assign A.right = B sau do .check nut B.left (y) gan vao A.right 
    # bo link to B 
    # sau khi gan y vao A.right . update y.parent is A=> check if b.left is not None
    # B.left.parent =A sau do B.parent se la dc assign A.Parent
    # check if A.parent None assign self.root=b
    # a parent not None check NUT A name ben trai or ben phai Parent
    # assign B => gan A bang B left . A.parent =B
    def left_rotate(self, A):
        B = A.right  
        A.right = B.left 
        if B.left is not None:
            B.left.parent = A 
        B.parent = A.parent  # 
        if A.parent is None:  
            self.root = B ### chu Y 
        elif A == A.parent.left:
            A.parent.left = B
        else:
            A.parent.right = B
        B.left = A  
        A.parent = B 


    def right_rotate(self, A):
        B = A.left  # B becomes the new root of this subtree
        A.left = B.right  # Move B's right child to A's left
        if B.right is not None:
            B.right.parent = A  # Update B.right's parent to A
        B.parent = A.parent  # B takes A's parent
        if A.parent is None:  # A was the root
            self.root = B
        elif A == A.parent.right:
            A.parent.right = B
        else:
            A.parent.left = B
        B.right = A  # A becomes the right child of B
        A.parent = B  

    def print_tree(self, node, indent="", last=True):
        if node is not None:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "   "
            else:
                print("L----", end="")
                indent += "|  "
            color = "RED" if node.color == "RED" else "BLACK"
            print(f"({node.data}, {color})")
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)


# Example usage:
if __name__ == "__main__":
    tree = RedBlackTree()
    elements = [30, 20, 40, 10, 25, 35, 50]
    for el in elements:
        tree.insert(el)

    tree.print_tree(tree.root)




