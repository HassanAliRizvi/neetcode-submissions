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
        string = ""
        for strings in strs:
            string_length = len(strings)
            string += str(string_length) + "#" + strings
        
        return string


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            hash_index = i

            while s[hash_index] != "#":
                hash_index += 1
                
            string_length = int(s[i:hash_index]) # 4#neet
            string = s[hash_index + 1: hash_index + 1 + string_length]
            result.append(string)
            
            i = string_length + hash_index + 1

        return result

        '''
        result = []
        i = 0  # Start index
        
        while i < len(s):
            hash_index = i

            # Find the '#' that separates the length from the actual string
            while s[hash_index] != "#":
                hash_index += 1
            
            # Get the length of the next string
            string_length = int(s[i:hash_index])  # 4#neet
            # Extract the string using the length and hash index
            string = s[hash_index + 1: hash_index + 1 + string_length]
            result.append(string)
            
            # Move i to the start of the next encoded part
            i = hash_index + 1 + string_length

        return result

        '''

                






