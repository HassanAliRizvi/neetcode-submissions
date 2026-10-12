class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for wrd in word:
                wrd = ord(wrd) - ord('a')
                count[wrd] += 1
            
            res[tuple(count)].append(word)
        
        return list(res.values())
        


        # space = O(m)
        # time = O(n) * O(m log m)
            


        