class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_numbers = {}

        for index, value in enumerate(nums):
            if value not in hash_numbers:
                hash_numbers[value] = index
            diff = target - value
            if diff in hash_numbers and hash_numbers[diff] != index:
                return [hash_numbers[diff], index]
        

        