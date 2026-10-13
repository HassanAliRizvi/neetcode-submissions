class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {} # {1:1, 2:2, 3:2}
        for num in nums:
            if num not in dict_nums:
                dict_nums[num] = 1
            dict_nums[num] += 1
        
        freq = [[] for _ in range(len(nums)+2)]
        for key,value in dict_nums.items():
            freq[value].append(key)
        
        res = []
        count = 0
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                count += 1
                if count == k:
                    return res

        






