class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        resSet = set(nums)
        res = 0
        for num in nums:
            if (num-1) not in resSet:
                length = 0
                while (num+length) in resSet:
                    length += 1
            
                if length > res:
                    res = length
        
        return res