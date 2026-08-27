class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        string_lower = s.lower()
    
        while i < j:
            while not string_lower[i].isalnum() and i < j:
                i += 1
            while not string_lower[j].isalnum() and j > i:
                j -= 1
            if string_lower[i] != string_lower[j]:
                return False
            i += 1
            j -= 1
            
        
        return True