# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        """
        [1,2,3,4], n = 2
        """
        # find length
        curr = head # curr = [1,2,3,4], n = 2
        length = 0 # 

        while curr != None:
            length += 1 # 4
            curr = curr.next


        if n == length: # n = 2 != length
            return head.next # 

        # move to node before the one we want to remove
        curr = head
        count = 1

        while curr != None:
            if count == length - n: # count == (4-2) -> 1 != 2 2 == 2 tick
                curr.next = curr.next.next
                break

            count += 1
            curr = curr.next

        return head
        
            
        