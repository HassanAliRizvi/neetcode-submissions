class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        ["Hello", "World"]
        res = 4#Hello5#World

        """
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res


    def decode(self, s: str) -> List[str]:

        list_res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1:length+j+1]
            list_res.append(word)

            i = length+j+1

        return list_res
