class Solution:
    def findMin(self, nums: List[int]) -> int:

        """ 
        n is the rotation how many times
        
        [3,4,5, 6,1,2] -> [3,4,5,6,7]
        [4,5,0, 1,2,3]
        [4,5, 6,7]

        """
        """
        #binary_search simple approach
        l,r = 0, len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]   

        """
        #recrusive approach    
        def binarySearch(l,r):
            if l >= r:
                return nums[l]
            
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                return binarySearch(mid+1,r)
            else:
                return binarySearch(l,mid)
        
        return binarySearch(0,len(nums)-1)
