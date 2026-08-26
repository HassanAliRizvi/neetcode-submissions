class Solution:

    def encode(self, strs: List[str]) -> str:
        stringRes = ""
        for string in strs:
            stringRes += str(len(string)) + "#" + string
        
        return stringRes
    def decode(self, s: str) -> List[str]:
        #---->   4#leet4#code
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            letter = s[j+1:j+1+length]
            res.append(letter)
            i = j+1+length
        return res


