class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        countMap = {} # {1:1,2:3,3:3}

        for n in nums:
            countMap[n]  = countMap.get(n, 0) + 1
        
        for key,values in countMap.items():
            freq[values].append(key)


        res = []

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res