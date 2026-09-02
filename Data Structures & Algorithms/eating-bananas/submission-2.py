class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k = banana / hour
        h = hours
        piles[i] = number of bananas in that pile
        if pile[i] < k:
            h -= 1
        
        [1,4,3,2] = 10 bananas, 9 hours
        [1,2,2,1] = 11 banaas total. 2 for each pile
        [1]
        1,1,1,1,1,1 = 6 hours < 9 hours
        [1,2,3,4,5,6,7,8,9] = you may DECIDE k (banana/hour)
        need to find a target k which is less than 9
        """

        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            totalHours = 0

            for p in piles:
                totalHours += math.ceil(float(p) / k)
            
            if totalHours <= h:
                r = k - 1
            
            else:
                l = k + 1
        
        return l


        



        

        
