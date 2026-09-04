class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        nums=[3,5,6 ,0,1,2], target=4
              l          r
        
        

        """
        l,r = 0, len(nums) - 1

        while l <= r:
            midPoint = (l+r) // 2
            if nums[midPoint] == target:
                return midPoint

            #left sorted array NOT left ascending sorted array
            if nums[l] <= nums[midPoint]:
                if nums[l] > target or nums[midPoint] < target:
                    l = midPoint + 1
                else:
                    r = midPoint - 1
            
            else:
                if nums[r] < target or nums[midPoint] > target:
                    r = midPoint - 1
                else:
                    l = midPoint + 1
        
        return -1 
            



        