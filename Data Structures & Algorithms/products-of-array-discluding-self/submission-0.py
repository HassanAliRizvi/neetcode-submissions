class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1 = [1] * len(nums) # [1,2,4,6] -> [1,1,2,8]
        list2 = [1] * len(nums) # [1,2,4,6] -> [48,24,6,1]  []
        res = [0] * len(nums)
        
        for i in range(1,len(list1)):
            list1[i] = list1[i-1] * nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            list2[i] = list2[i+1] * nums[i+1]
         
        for i in range(len(nums)):
            res[i] = list1[i] * list2[i]
        
        return res