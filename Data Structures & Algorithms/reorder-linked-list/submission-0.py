# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        """
        [0, n-1, 1, n-2, 2, n-3, ...]
        [0, 1, 2, 3, 4, 5, 6]

        0, 7-1(6), 1, 7-2(5), 2, 
        pattern: 0, len(num) - count, count, len(num) - count
        count = 0 + 1 + 1
        
        {0:0, 1:1, 2:2, 3:3, 4:4...}
        value:index
        no duplicate numbers
        """

        # fast and slow pointer approach
        # find the middle of the linked list and then reverse the second half

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None

        prev = None

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        fast = prev

        tail = head
        slow = head

        while fast != None:
            temp1 = slow.next
            temp2 = fast.next

            slow.next = fast
            fast.next = temp1

            slow = temp1
            fast = temp2

        #return temp.next
        

        

        """

        BRUTE FORCE O(N) time AND space
        
        listFreq = [] # [[0,0], [1,1], [2,2], [3,3], [4,4], [5,5]}
        curr = head
        count = 0
        
        while curr!= None:
            listFreq.append([curr,count])
            count += 1
            curr = curr.next
        
        newList = [0] * len(listFreq)
        pattern = 0
        for i in range(1,len(newList)):
            newList[i] = listFreq[(len(listFreq)-1)-pattern][0]
            pattern += 1
        
        return newList
        """ 
        