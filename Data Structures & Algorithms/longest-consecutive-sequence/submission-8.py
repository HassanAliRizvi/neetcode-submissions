class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        nums = [2,20,4,10,3,4,5]

        [2,20,4,10,3,5]

        while 

        len(num) = 4
        [1,1,1,1]


        """
        set_nums = set(nums)
        counter = 0

        for num in set_nums: # O(n)
            count = 0
            if (num-1) not in set_nums:
                consecutive_num = num
                while consecutive_num in set_nums: # O(n)
                    count += 1
                    consecutive_num += 1
            counter = max(count, counter)
        
        return counter
                


        