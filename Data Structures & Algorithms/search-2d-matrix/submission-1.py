class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ 
        matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
                       l r
                                 l                         r
        """
        list_length = len(matrix)

        # binary search for all the whole list
        list_l, list_r = 0, list_length - 1
        while list_l <= list_r:
            mid_list = (list_l + list_r) // 2
            if matrix[mid_list][-1] < target:
                list_l = mid_list + 1
            
            elif matrix[mid_list][0] > target:
                list_r = mid_list - 1

            else:
                break
        
        if list_l > list_r:
            return False


        # binary search for each row
        row_length = len(matrix[0])
        row = (list_l+list_r)//2
        l, r = 0, row_length - 1
        while l <= r:
            mid_row = (l+r) // 2
            if matrix[row][mid_row] < target:
                l = mid_row + 1
            
            elif matrix[row][mid_row] > target:
                r = mid_row - 1
            
            else:
                return True
        
        return False


