class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0

        """
        set = (X,Y) count = 1 + 1 = 2
        length = j - i + 1

        XYYX

        if s[r] in set then remove elements in set
        if the element is not in set:
            add it 
            length += 1
        
        if it's:
            s_set = set()
        
        XYZ k = 1

        X,Y,Z

        AAABABB



        """

        count = {}
        l,r = 0,0
        max_length = 0
        res = 0

        while r < len(s):
            count[s[r]] = count.get(s[r],0) + 1

            if (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r-l+1))
            
            r+= 1
        
        return res
            

        