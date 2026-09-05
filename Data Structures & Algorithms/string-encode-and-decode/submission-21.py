class Solution:

    def encode(self, strs: List[str]) -> str:

        """
        4#Hello4#World

        """
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        
        print(res)
        return res
        


    def decode(self, s: str) -> List[str]:
        res  = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!="#":
                j += 1
            length_of_word = int(s[i:j])
            word = s[j+1: length_of_word+j+1]
            i = length_of_word+j+1 # to get to pound sign
            res.append(word)

        return res








        
