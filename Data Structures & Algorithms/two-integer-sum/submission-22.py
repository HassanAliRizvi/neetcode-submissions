class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for index,value in enumerate(nums):
            diff = target - value
            if diff in nums_map:
                return [nums_map[diff],index]
            nums_map[value] = index

        