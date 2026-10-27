class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
            # "5#Hello5#World"
            #  ij     i
        return res 
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!="#":
                j += 1
            string_length = s[i:j]
            string = s[j+1:int(string_length)+j+1]
            i = int(string_length) + j + 1
            res.append(string)
        return res