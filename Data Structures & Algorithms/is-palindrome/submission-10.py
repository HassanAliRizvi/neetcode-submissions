class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()

        i,j = 0,len(s)-1

        while i<j:
            if not s_lower[i].isalnum():
                i += 1
                continue
            if not s_lower[j].isalnum():
                j -= 1
                continue
            
            if s_lower[i] != s_lower[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
        