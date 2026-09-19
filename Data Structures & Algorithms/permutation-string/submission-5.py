class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_dict = {}
        for s in s1:
            s1_dict[s] = 1 + s1_dict.get(s,0)
        
        
        check = len(s1_dict)
        for r in range(len(s2)):
            l = r
            count = 0
            s2_dict = {}
            while l < len(s2):
                s2_dict[s2[l]] = 1 + s2_dict.get(s2[l],0) 

                if s2_dict[s2[l]] > s1_dict.get(s2[l],0):
                    break
                
                if s2_dict[s2[l]] == s1_dict.get(s2[l],0):
                    count += 1
                
                if count == check:
                    return True
                
                l += 1
        
        return False

        