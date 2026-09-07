class Solution:
    def isValid(self, s: str) -> bool:

        """
        s = "([{}])"

        res_stack = [ ([{ ]

        dict = {')':'(', ']':'[', '}':'{'}
        
        [()

        """
        if s == "":
            return []

        dict_hash = {']':'[','}':'{',')':'('}

        res_stack = []

        for parens in s:
            if parens not in dict_hash:
                res_stack.append(parens)
            elif res_stack and res_stack[-1] == dict_hash[parens]:
                res_stack.pop()
            else:
                return False
        
        return True if not res_stack else False


        




        

        