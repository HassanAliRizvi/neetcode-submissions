class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        """
        ["1","2","+","3","*","4","-"]
        res = [1,2] -> [3,3] -> [9,4] -> [5]

        """
        res = []

        for tkr in tokens:
            if tkr == "+":
                num1 = res.pop()
                num2 = res.pop()
                res.append(int(num1)+int(num2))
            
            elif tkr == "*":
                num1 = res.pop()
                num2 = res.pop()
                res.append(int(num1)*int(num2))
            
            elif tkr == "-":
                num1 = res.pop()
                num2 = res.pop()
                res.append(int(num2)-int(num1))
            
            elif tkr == '/':
                num1 = res.pop()
                num2 = res.pop()
                res.append(int(num2)/int(num1))
            else:
                res.append(tkr)
        return int(res[0])


        