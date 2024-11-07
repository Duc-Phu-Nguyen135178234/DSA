# # Tables

# ADT
# Consists of a set of unordered records
# Records are key-value pairs
# Within a table, keys are unique
# Operations:

# insert(key, value)
# modify(key, value)
# search(key)
# remove(key)
# Implementations:

# Sorted Array: Slow to insert/remove, search is fast (binary search), modify is fast
# Unsorted Array: Fast to insert, everything else is slow
# Hash Tables
# Use a hash function to determine where to put the record.
# Basic Algorithm: A hash table is basically an array.
# •	hashvalue = hash(key);
# •	hashindex = hashvalue % capacity of array
# The hashindex is where a record goes.
# Collision
# •	Collision: When two records with unique keys end up at the same hashindex.
# o	Number of possible keys > number of hash values > number of hash indexes.
# o	Pigeonhole Principle: If there are n items categorized into m categories and n > m, there will be a category where there are 2 items.
# Collision Resolution
# Since collisions can’t be entirely eliminated, they must be handled.
# Closed Addressing
# •	At each array position, store a "list" of records.
# o	Array-based list: bucketing
# o	Linked-based list: chaining
# •	The capacity of the table should be equal to the number of records you plan to store.
# Open Addressing
# •	If the spot at hashindex is not available, put the record in the next available spot.
# o	Linear Probing: Increment to the next index, wrapping around if necessary.
# o	Quadratic Probing (not covered in course): 1, 4, 9, 16, etc.
# o	Double Hashing: Use a second hash function.
# Removing in open addressing can be challenging:
# •	Tombstoning: Leave a marker for deleted records
# •	Non-tombstoning: Manage deletions differently





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
# chu y function insert when get out while need to insert key value
# remove function last line curr=(curr+1)%self.cap
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
            curr=(curr+1)%self.cap ### Chu Y

 

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
