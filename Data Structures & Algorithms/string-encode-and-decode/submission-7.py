class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        Clarifying questions
        1) empty string? Return empty, zero?
        2) does the decode automatically pass in the return string of encode into decode

        Constraints:
        1) strs[i] contains only UTF-8 characters.
        2) 

        '''
        ''' 

        Approach: Input: [''#,"neet","code","love","you"]
        input: ['4, ''5']
        string = 4#neet#4code
                 i j
                 


        '''
        result = ''
        for string in strs:
            result += str(len(string)) + "#" + string
        
        return result



    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while (s[j] != '#'):
                j += 1
            string_length = int(s[i:j]) # 4# ij
            actual_string = s[j+1:j+string_length+1] # 
            res.append(actual_string)
            i = j+string_length+1
        
        return res

        


