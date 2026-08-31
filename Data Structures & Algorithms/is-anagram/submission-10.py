class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        #dict2 = {}

        for word in s:
            dict1[word] = 1 + dict1.get(word,0)
        
        for word in t:
            if word in dict1:
                dict1[word] -= 1
            else:
                return False
        
        for value in dict1.values():
            if value!=0:
                return False
        
        return True
