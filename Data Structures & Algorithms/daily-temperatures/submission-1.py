class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res_stack = []
        res = [0] * len(temperatures)


        for i,v in enumerate(temperatures):
            while res_stack and v > res_stack[-1][1]:
                index, value = res_stack.pop()
                res[index] = i - index
            res_stack.append([i,v])
        
        
        return res


        