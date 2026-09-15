# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        """
        head = [1,2,3,4,5,6], k = 3

        """
        count = 0
        curr = head
        dummy_node = ListNode()
        tail = dummy_node

        while curr:
            check = curr
            
            while check and count < k:
                check = check.next
                count += 1
            
            if count < k:
                tail.next = curr
                break

            old_head = curr

            prev = None
            count = k

            while count > 0:
                temp = curr.next # temp = 1.next = 2
                curr.next = prev # 1.next = None
                prev = curr # None = 1
                curr = temp # 1 = 2
                count -= 1

            tail.next = prev
            tail = old_head

        return dummy_node.next     