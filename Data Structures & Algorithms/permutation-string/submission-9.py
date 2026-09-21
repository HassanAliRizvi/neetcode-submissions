class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {} # {a:1,b:1,c:1}
        s2_dict = {} 

        for char in s1:
            s1_dict[char] = 1 + s1_dict.get(char,0)
        
        l,count = 0, 0
        for r in range(len(s2)):
            rightChar = s2[r]
            s2_dict[rightChar] = 1 + s2_dict.get(rightChar, 0)

            if s1_dict.get(rightChar,0) == s2_dict[rightChar]:
                count += 1

            while s2_dict[rightChar] > s1_dict.get(rightChar, 0):
                leftChar = s2[l]

                if s2_dict[leftChar] == s1_dict.get(leftChar, 0):
                    count -= 1

                s2_dict[leftChar] -= 1
                l += 1

            if len(s1_dict) == count:
                return True
        
        return False



        