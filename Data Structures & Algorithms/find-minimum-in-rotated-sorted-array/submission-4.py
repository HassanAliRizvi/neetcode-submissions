class Solution:
    def findMin(self, nums: List[int]) -> int:

        """

        nums = [3,4,5,6,1,2]

        nums = [4,5,0,1,2,3]
        
        nums = [5,0,1,2,3,4]


        """

        l, r = 0, len(nums) - 1

        while l<r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


        