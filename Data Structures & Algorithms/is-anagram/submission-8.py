class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for word in s:
            dict1[word] = 1 + dict1.get(word,0)
        
        for word in t:
            dict2[word] = 1 + dict2.get(word,0)
        

        return dict1 == dict2
