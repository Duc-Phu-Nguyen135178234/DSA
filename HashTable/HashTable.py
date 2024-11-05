

# An abstract data type (ADT).

# A collection of key–value pairs. A key–value pair is sometimes called Record.
# This collection is not ordered. Each key is unique within the collection.

# Insert(key, value) – add a key–value pair to the table
# Modify(key, value) – modifies a key–value pair
# Remove(key) – removes a record that has a matching key
# Search(key) – find a record given a particular key – O(log n)
# Create a table using a sorted array

# Sorted array based on the key (ignore the value)
# Sorted Arrays have the ability to do a binary search.

# Linear search – O(n) where n is number of items in array
# Binary search – can only be done if array is sorted. Also requires "random" access to each element. O(log n)
# Search() – O(log n)
# Remove(key) – O(log n) for the search + actual removal O(n)
# Insert(key, value) – O(n)
# Modify(key, value) – O(log n) for search + actual modification O(1)

# Unsorted Array?

# Search() – O(n)
# Insert() – O(1)
# Remove() – O(n) for search + actual removal O(n) → O(n)
# Modify() – O(n) for search + actual modification O(1) → O(n)


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

# Hash Table using LinearProbing is Opening Address       
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
