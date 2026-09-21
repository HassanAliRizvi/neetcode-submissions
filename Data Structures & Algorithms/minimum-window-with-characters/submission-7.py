class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        s = "OUZODYXAZV", t = "XYZ"
                  l
                      r

        dict_t = all letters in t

        len(l,r) == len(t) then we will add the string to res

        max(t,s) -> if len(l,r) < len(res): res = len(l,r) 
        """
        # populate all the letters from t to a dict to 
        # keep count of frequencies. 
        dict_t = {}
        for char in t:
            dict_t[char] = 1 + dict_t.get(char,0)

        
        res, resLen = [-1,-1], float("infinity")
        count, need, l = 0, len(dict_t), 0
        dict_s = {}
        for r in range(len(s)):
            charRight = s[r]
            dict_s[charRight] = 1 + dict_s.get(charRight,0)

            if dict_s[charRight] == dict_t.get(charRight,0):
                count += 1
        
            while count == need:
                if (r-l+ 1) < resLen:
                    resLen = (r-l+1)
                    res = [l,r]
                charLeft = s[l]
                dict_s[charLeft] -= 1

                if dict_s[charLeft] < dict_t.get(charLeft,0):
                    count -= 1
                l += 1
        
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""





        
