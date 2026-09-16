# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ 

        lists = [[1,2,4],[1,3,5],[3,6]]

        [0] -> [1] -> [2] -> 1-> 4 [4] -> 1


        """
        if not lists:
            return None

        def mergeTwoLists(list1,list2):
            dummyNode = ListNode()
            tail = dummyNode

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                
                tail = tail.next

            tail.next = list1 if list1 else list2
            return dummyNode.next
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None 
                mergedLists.append(mergeTwoLists(list1,list2))
            lists = mergedLists
        
        return lists[0]

            

        





        