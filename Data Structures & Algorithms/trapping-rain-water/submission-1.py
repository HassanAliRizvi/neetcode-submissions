class Solution:
    def trap(self, height: List[int]) -> int:

        """ 

        0,2,0,3,1,0,1,3,2,1
        2 - 0 = 2

        """

        l, r = 0, len(height) - 1

        current_left, current_right = 0, 0
        trapped = 0

        while l < r:
            current_left = max(height[l],current_left)
            current_right = max(height[r],current_right)

            if height[l] < height[r]:
                trapped += (current_left-height[l])
                l += 1
            
            else:
                trapped += (current_right-height[r])
                r -= 1
            
        return trapped



        