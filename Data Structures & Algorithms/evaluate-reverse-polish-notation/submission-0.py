class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """ 

        ["1","2","+","3","*","4","-"]

        a = [1,2]
        + pop() pop()

        [1,+,2,3,*4]
        [1+]

        """
        res = []
        tk = 0
        for tk in tokens:
            if tk == "+":
                num1 = res.pop()
                num2 = res.pop()
                res.append(num1+num2)
            elif tk == "-":
                num1 = res.pop()
                num2 = res.pop()
                res.append(num2-num1)
            elif tk == "*":
                num1 = res.pop()
                num2 = res.pop()
                res.append(num1*num2)
            elif tk == "/":
                num1 = res.pop()
                num2 = res.pop()
                res.append(int(num2/num1))
            else:
                res.append(int(tk))


        return res[0]

                