# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        0 -> 1 -> 2 -> 3 -> null
        3 -> 2 -> 1 -> 0 -> null
        """
        curr = head
        prev = None
        while curr:
            next_node = curr.next # next_node = 1
            curr.next = prev # 
            prev = curr
            curr = next_node
        return prev

        

        