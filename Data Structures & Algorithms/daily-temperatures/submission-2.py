class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """

        while stack is not empty and current value is greater the value in stack

        """

        res_stack = []
        res = [0] * len(temperatures)


        for i,v in enumerate(temperatures):
            while res_stack and res_stack[-1][1] < v:
                index, value = res_stack.pop()
                res[index] = i - index
            res_stack.append([i,v])
        
        
        return res


        