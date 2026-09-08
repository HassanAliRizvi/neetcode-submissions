class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """

        [4,1,0,7] [2,2,1,1]
        time = (target - position) / speed
        (10-4)/2 = 6/2 = 3
        (10-1)/2 = 9/2 = 4.5 + 1
        (10-0)/1 = 10 + 1
        (10-7)/1= 3/1 = 3 + 1

        (10-4)/2 = 6/2 = 3
        (10-7)/1= 3/1 = 3 + 1
        (10-1)/2 = 9/2 = 4.5 + 1
        (10-0)/1 = 10
        (10-1)/2 = 4.5
        (10-4)/2 = 3


        """
        cars = sorted(zip(position,speed),reverse=True)

        res = []
        for p,s in cars:
            time = (target - p) / s
            res.append(time)
            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()     
        return len(res)

        