class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_dict = {}
        for s in s1:
            s1_dict[s] = 1 + s1_dict.get(s,0)
        
        
        check = len(s1_dict)
        for l in range(len(s2)):
            r = l
            count = 0
            s2_dict = {}
            while r < len(s2):
                s2_dict[s2[r]] = 1 + s2_dict.get(s2[r],0) 

                if s2_dict[s2[r]] > s1_dict.get(s2[r],0):
                    break
                
                if s2_dict[s2[r]] == s1_dict.get(s2[r],0):
                    count += 1
                
                if count == check:
                    return True
                
                r += 1
        
        return False

        