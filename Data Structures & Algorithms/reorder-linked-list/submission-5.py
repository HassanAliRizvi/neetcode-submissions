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
        fast = head
        """
        [0, 1, 2, 3, 4, 5, 6]
                  s        f
        [0,1,2,3]
        [4,5,6]
             f

        """

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        # fast is now [4->5->6]
        slow.next = None
        # slow is now [0,1,2,3 -> None]
        # curr = fast # curr = 6
        prev = None
        #reverse the linked list fast
        while curr!=None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        fast = prev # this is set to 6 now
        slow = head # this is set to the head pointer 1

        # merge the arrays
        while fast!=None:
            temp1 = slow.next # 2
            temp2 = fast.next # None

            slow.next = fast # 1.next = 6
            fast.next = temp1 # 6.next = 2

            slow = temp1 # slow = temp1 (2)
            fast = temp2 # fast = temp2 (5)

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
        