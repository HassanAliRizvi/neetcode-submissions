class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,4,6] -> [1,1,2,8] [48,24,6,1]
        res = [1] * len(nums)

        prefix = 1
        for i in range(1,len(nums)):
            prefix *= nums[i-1]
            res[i] = prefix
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        