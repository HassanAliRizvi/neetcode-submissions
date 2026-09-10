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
        curr = head 
        length = 0 

        # we calculate length that way if length == n then it means remove the first element of the list
        # which means head.next
        while curr != None:
            length += 1 # 4
            curr = curr.next
        if n == length: 
            return head.next

        # if n!= then we run the below code
        # we keep track of count and see if count == (length - n) why length - n?
        # BECAUSE question says to delete nth node FROM THE END 
        # if it said from the BEGINNING then we would have done count == n
        curr = head
        count = 1

        while curr != None:
            if count == length - n: # count == (4-2) -> 1 != 2 2 == 2 great! now connect the current node to the node that is next to next 
                curr.next = curr.next.next
                break

            count += 1
            curr = curr.next

        return head
        
            
        