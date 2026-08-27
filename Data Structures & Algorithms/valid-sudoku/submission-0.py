class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        setRow = [set() for _ in range(9)]
        setCol = [set() for _ in range(9)]
        setSubBoxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue
            
                if num in setRow[r]:
                    return False
                
                setRow[r].add(num)

                if num in setCol[c]:
                    return False
                
                setCol[c].add(num)

                box_index = (r//3, c//3)
                if num in setSubBoxes[box_index]:
                    return False
                
                setSubBoxes[box_index].add(num)

        return True





        
            
            
            
