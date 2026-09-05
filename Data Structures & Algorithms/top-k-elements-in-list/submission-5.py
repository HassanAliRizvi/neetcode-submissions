class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_res = {}
        freq = [[] for _ in range (len(nums)+1)] # [1,2,3]
        res = []

        for num in nums:
            if num in dict_res:
                dict_res[num] += 1
            else:
                dict_res[num] = 1
        
        for key,value in dict_res.items():
            freq[value].append(key)
        
        count = 0
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                if count == k:
                    break
                count += 1
                res.append(num)
        
        return res


