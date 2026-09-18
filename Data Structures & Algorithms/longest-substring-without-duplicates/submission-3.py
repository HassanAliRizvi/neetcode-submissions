class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,1
        string_set = set()

        """

        zxyzxyz
           j
          i
        [z,x,y,z] -> [x,y]

        """
        i,j = 0,0
        count = 0
        max_count = 0

        while j < len(s):
            while s[j] in string_set:
                string_set.remove(s[i])
                i += 1
            
            string_set.add(s[j])
            max_count = max(max_count,j-i+1)
            j += 1
        
        return max_count
        