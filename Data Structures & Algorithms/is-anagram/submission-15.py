class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        for word in s:
            s_dict[word] = 1 + s_dict.get(word,0)

        t_dict = {}
        for word in t:
            t_dict[word] = 1 + t_dict.get(word,0)

        
        for key,value in s_dict.items():
            if key not in t_dict:
                return False
            t_dict[key] -= 1
            s_dict[key] -= 1
        
        return True if t_dict == s_dict else False