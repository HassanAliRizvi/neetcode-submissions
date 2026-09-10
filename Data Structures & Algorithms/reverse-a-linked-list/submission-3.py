# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None

        while curr != None:
            temp = curr.next # 1
            curr.next = prev # 0 -> None
            prev = curr # prev = 0
            curr = temp # curr = 1
        
        return prev
        