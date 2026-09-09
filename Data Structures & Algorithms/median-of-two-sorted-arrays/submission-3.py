class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        """
        l1,r1
        [1,3] if l1 <= r2 and l2 <= r1
        l2,r2 
        [2,4]

        [3,4,5] -> [1,2,3,4,5] -> 3 
        5 (total) - 2 (larger) = 3 // 2 = 1
        [1,2]

        [1,3] -> [1,2,3,4] -> 2+3 = 5/2 = 2.5
        [2,4]

        min(r1,r2) max(l1,l2) -> for odd number
            |
            ^
            for even is min(r1,r2) + max(l1,l2) / 2

        """
        smaller = []
        larger = []
        if len(nums1) < len(nums2):
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1
        
        l,r = 0, len(smaller) 
        while l<=r:
            midX = (l+r) // 2
            midY = (len(larger) + len(smaller) + 1) // 2 - midX
            l2 = smaller[midX] if midX < len(smaller) else float('inf')
            l1 = smaller[midX-1] if midX > 0 else float('-inf')
            r2 = larger[midY] if midY < len(larger) else float('inf')
            r1 = larger[midY-1] if midY > 0 else float('-inf')
        
            if l1 <= r2 and r1 <= l2:
                if (len(larger) + len(smaller)) % 2 == 0:
                    return (max(l1, r1) + min(l2, r2)) / 2
                else:
                    return max(l1, r1)
            
            if l1 > r2:
                r = midX - 1
            else:
                l = midX + 1




        



        
        