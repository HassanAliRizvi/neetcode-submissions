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
        dict_t = {} # {X:1, Y:1, Z:1}
        res = ""

        for char in t:
            dict_t[char] = 1 + dict_t.get(char,0)
        
        dict_s = {}
        count, need = 0, len(dict_t)
        res, resLen = [-1,-1], float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]
            
            dict_s[char] = 1 + dict_s.get(char,0)
                
            if char in dict_t and dict_t[char] == dict_s[char]:
                count += 1
            #print("This is count" + str(count))

            while count == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)

                dict_s[s[l]] -= 1
                if s[l] in dict_t and dict_s[s[l]] < dict_t[s[l]]:
                    count -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen!=float("infinity") else ""


        
