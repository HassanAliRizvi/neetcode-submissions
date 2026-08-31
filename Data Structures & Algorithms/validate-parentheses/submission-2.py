class Solution:
    def isValid(self, s: str) -> bool:

        """
        s = "([{}])"

        res_stack = [ ([{ ]

        dict = {')':'(', ']':'[', '}':'{'}


        """

        res_stack = []
        paren_map = {')':'(', ']':'[', '}':'{'}

        for paren in s:
            if paren in paren_map:
                if not res_stack or res_stack[-1]!= paren_map[paren]:
                    return False
                res_stack.pop()
            else:
                res_stack.append(paren)

        print(res_stack)
        return True if not res_stack else False

        