class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """

        matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
                       l                          r


        """
        # iterate through the list and find the row
        l,r = 0, len(matrix) - 1
        row = 0
        while l<=r:
            mid = (l+r) // 2
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                row = mid
                break

        #iterate through the row
        #row = (l+r) // 2
        l_2,r_2 = 0, len(matrix[row]) - 1
        while l_2<=r_2:
            mid = (l_2+r_2) // 2
            if matrix[row][mid] < target:
                l_2  = mid + 1
            elif matrix[row][mid] > target:
                r_2 = mid - 1
            else:
                return True
        
        return False
        