class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {} # for s
        dict2 = {} # for t 
        # {key(letter): value(count of the letter)}
        # s car {c:1, a:1, r:1}
        if len(s) != len(t):
            return False
        
        for letter in s:
            if letter not in dict1:
                dict1[letter] = 0
            else:
                dict1[letter] += 1
        
        for letter in t:
            if letter not in dict2:
                dict2[letter] = 0
            else:
                dict2[letter] += 1
        
        return dict1 == dict2
        
