class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        res = set(nums)
        longest = 1
        for num in nums:
            count = 1
            if (num-1) not in res:
                consecutive_number = num + 1
                while consecutive_number in res:
                    consecutive_number += 1
                    count += 1
                    longest = max(longest,count)
        return longest