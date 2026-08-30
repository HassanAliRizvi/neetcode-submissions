class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        res = defaultdict(list)
        res_list = []

        for string in strs:
            sorted_string = "".join(sorted(string))
            res[sorted_string].append(string)
            
            
        
        return list(res.values())
            


        