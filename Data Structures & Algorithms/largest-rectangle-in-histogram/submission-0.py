class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        """

        heights = [7,1,7,2,2,4]

        output: 8



        """
        stack = []

        max_area = 0
        for index, height in enumerate(heights):
            start = index
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                start = j
                w = index - j 
                a = h * w
                max_area = max(a, max_area)
            stack.append((height, start))
            

        while stack != []:
            h, j = stack.pop()
            w = len(heights) - j
            max_area = max(max_area, h*w)
        
        return max_area
            




        