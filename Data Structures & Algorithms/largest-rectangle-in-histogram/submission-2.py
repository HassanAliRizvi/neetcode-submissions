class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0
        res_stack = [] # [index,height]

        for index,height in enumerate(heights):
            start = index
            while res_stack and res_stack[-1][1] > height:
                i,h = res_stack.pop()
                area = h * (index - i)
                max_area = max(area,max_area)
                start = i
            res_stack.append([start,height])
        

        while res_stack:
            index,height = res_stack.pop()
            area = height * (len(heights) - index)
            max_area = max(area,max_area)

        return max_area



        