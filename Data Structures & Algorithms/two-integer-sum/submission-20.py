class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dict_index = {}
       for index,value in enumerate(nums):
        diff = target - value
        if diff in dict_index:
            return [dict_index[diff], index]
        dict_index[value] = index
        


        