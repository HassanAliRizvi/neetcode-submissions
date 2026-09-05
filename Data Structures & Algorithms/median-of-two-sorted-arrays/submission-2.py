class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLength = len(nums1) + len(nums2)

        larger = []
        smaller = []

        if len(nums1) > len(nums2):
            larger = nums1
            smaller = nums2
        
        else:
            smaller = nums1
            larger = nums2

        l,r = 0, len(smaller)

        """
        x = [1,3] , 
        y = [2,4] 
        
        4+1 // 2 = 2 - 1 = 1


        """

        while l <= r:
            partitionX = (l+r) // 2 # mid number of smaller array
            partitionY = ((totalLength+1) // 2) - partitionX # mid number of Y

            #partition X
            l1 = float('-inf') if partitionX == 0 else smaller[partitionX-1]
            #element to the right of partition X
            r1 = float('inf') if partitionX == len(smaller) else smaller[partitionX]

            #partition Y
            l2 = float('-inf') if partitionY == 0 else larger[partitionY-1]
            # #element to the right of partition Y 
            r2 = float('inf') if partitionY == len(larger) else larger[partitionY]

            if l1 <= r2 and l2 <= r1:
                if totalLength % 2 == 0:
                    return (max(l1,l2) + min(r1,r2)) / 2
                else:
                    return float(max(l1,l2))
            
            elif l1 > r2:
                r = partitionX - 1
            else:
                l = partitionX + 1









        