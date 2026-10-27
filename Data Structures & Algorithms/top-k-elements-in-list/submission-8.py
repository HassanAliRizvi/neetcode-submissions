class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        for num in nums:
            frequency_dict[num] = 1 + frequency_dict.get(num,0)
        

        frequency_list = [[] for _ in range(len(nums)+1)]


        for key,value in frequency_dict.items():
            frequency_list[value].append(key)
        #print(frequency_list)        
        res = []
        count = 0
        for i in range(len(frequency_list)-1,0,-1):
            for num in frequency_list[i]:
                if count == k:
                    break
                count += 1
                res.append(num)
                        
        
        return res

        

        






