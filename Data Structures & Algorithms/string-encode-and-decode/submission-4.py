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


        '''
        result_string = ''
        for string in strs:
            string_length = len(string)
            result_string += str(string_length) + '#' + string 

        print(result_string)
        return result_string



    def decode(self, s: str) -> List[str]:
        result = []
        length_string = len(s)
        i = 0
        while i < length_string:
            #  '#4neet#4code#4love#3you'
            j = i
            while s[j] != '#':
                j+= 1
            s_length = int(s[i:j])
            i = j + 1
            j = i + s_length
            result.append(s[i:j])
            i = j


        return result

                






