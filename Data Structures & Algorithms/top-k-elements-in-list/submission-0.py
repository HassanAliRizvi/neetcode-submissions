class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {} # less than O(n)
        # [1,2,3,2]
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            countMap[num] = countMap.get(num,0) + 1
        
        for num,count in countMap.items():
            freq[count].append(num)
        
        res = []

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
            
        

        

        


        