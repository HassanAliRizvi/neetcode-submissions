class Solution:
    def trap(self, height: List[int]) -> int:
        """
        [0,2,0,3,1,0,1,3,2,1]
        two pointers will be i and j
        i will be incremented if height [i] < height[j]
        if height[j] > height[i] 
            get differnce of height[j - i]
            add it to res
        
        [0,2,0,3,1,0,1,3,2,1]
           i   j 

        """

        l, r = 0, len(height)-1
        trapped = 0
        left_max,right_max = 0,0

        while l<r:

            left_max = max(left_max,height[l])
            right_max = max(right_max,height[r])

            if left_max < right_max:
                trapped += left_max - height[l]
                l += 1
            
            else:
                trapped += right_max - height[r]
                r -= 1
        
        return trapped
            

            


            







        