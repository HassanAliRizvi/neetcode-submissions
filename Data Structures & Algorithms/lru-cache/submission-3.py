class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None # None node
        self.next = None # None node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.cache = {}
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self,node):
        nxt = self.right
        prev = self.right.prev

        # establish the two way connection for the end node
        nxt.prev = node
        node.next = nxt

        # establish the two way connection for the 2nd last node
        node.prev = prev
        prev.next = node
    
    def remove(self,node):
        # get the previous and next nodes
        nxt = node.next
        prev = node.prev

        # establish the two way connection between left and right nodes of NODES
        prev.next = nxt
        nxt.prev = prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        
