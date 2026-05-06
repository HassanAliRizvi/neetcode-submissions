class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_dict = {}
        word_dict_t = {}
        if len(s) != len(t):
            return False
        
        for word in s:
            if word in word_dict:
                word_dict[word] += 1
            
            else:
                word_dict[word] = 1

        
        for word in t:
            if word in word_dict_t:
                word_dict_t[word] += 1
            
            else:
                word_dict_t[word] = 1
        
        return word_dict == word_dict_t


        