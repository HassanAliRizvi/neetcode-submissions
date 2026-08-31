class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for _ in range(len(board))]
        row = [set() for _ in range(len(board))]
        sub_boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                brd = board[r][c]

                if brd != '.':

                    if brd in col[c]:
                        return False
                    col[c].add(brd)

                    if brd in row[r]:
                        return False
                    row[r].add(brd)

                    sub_row_col = (r//3,c//3)
                    if brd in sub_boxes[sub_row_col]:
                        return False
                    sub_boxes[sub_row_col].add(brd)
        
        return True

        