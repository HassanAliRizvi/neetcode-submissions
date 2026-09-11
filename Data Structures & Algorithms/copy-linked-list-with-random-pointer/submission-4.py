"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        head = [[3,null],[7,3],[4,0],[5,1]]


        Output: [[3,null],[7,3],[4,0],[5,1]]
        three values
        1) .next
        2) .random
        3) .value

        .random mapping will get us to the count
        if index_count[.random] in dict:
            [3,index_count[.random]]

        """
        deep_copy_dict = {}
        curr = head
        while curr:
            deep_copy_dict[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = deep_copy_dict[curr]
            if curr.next:
                copy.next = deep_copy_dict[curr.next]
            
            if curr.random:
                copy.random = deep_copy_dict[curr.random]
            
            curr = curr.next
        
        if head is None:
            return None
        else:    
            return deep_copy_dict[head]
        
    




