class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLength = len(nums1) + len(nums2)

        larger = []
        smaller = []

        if len(nums1) > len(nums2):
            larger = nums1
            smaller = nums2
        
        else:
            larger = nums2
            smaller = nums1
        
        l, r = 0, len(smaller)

        while l <= r:
            partitionX = (l+r) // 2
            partitionY = (totalLength+1) // 2 - partitionX
            l1 = float('-inf') if partitionX == 0 else smaller[partitionX-1]
            r1 = float('inf') if partitionX == len(smaller) else smaller[partitionX]

            l2 = float('-inf') if partitionY == 0 else larger[partitionY-1]
            r2 = float('inf') if partitionY == len(larger) else larger[partitionY]

            #Valid partition
            if l1 <= r2 and l2 <= r1:
                if totalLength % 2 == 0:
                    return (max(l1,l2) + min(r1,r2)) / 2
                else:
                    return max(l1,l2)
            
            if l1 > r2:
                r = partitionX - 1
            
            else:
                l = partitionX + 1
            





        