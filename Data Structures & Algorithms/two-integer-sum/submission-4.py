class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff],index]
            
            num_map[num] = index
        