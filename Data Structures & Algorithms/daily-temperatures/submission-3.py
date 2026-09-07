class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        """
        [30,38,30,36,35,40,28]

        stack = [ [38,1], [30,2], [36,3]]
        


        """

        stack = []
        res = [0] * len(temperatures)

        for index,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                cur_stack_item = stack.pop()
                stack_index = cur_stack_item[1]
                res[stack_index] = index - stack_index
            else:
                stack.append([temp,index])

        return res
        