class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        0,1,2,3,4
        
        """
        
        l,r = 1,max(piles)
        res = 0
        while l<=r:
            total_time = 0
            mid = (l+r) // 2
            for pile in piles:
                total_time += math.ceil((pile) / mid)
            
            if total_time > h:
                l = mid + 1
            
            else:
                res = mid
                r = mid - 1
        
        return res

            
                


        