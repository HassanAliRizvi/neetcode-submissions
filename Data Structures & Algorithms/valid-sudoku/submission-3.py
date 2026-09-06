class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        row = [[] for each row]
        col = [[] for each col]
        subboxes = [[] for each subbox]

        """
        row = [set() for i in range(0,9)]
        col = [set() for i in range(0,9)]
        subBox = defaultdict(list)
        for r in range(0,9):
            for c in range(0,9):
                cell = board[r][c]

                if cell == ".":
                    continue

                if cell in row[r]:
                    return False
                row[r].add(cell)

                if cell in col[c]:
                    return False
                col[c].add(cell)

                row_and_col = (r//3, c//3)
                if board[r][c] in subBox[tuple(row_and_col)]:
                    return False
                else:
                    subBox[tuple(row_and_col)].append(board[r][c])
        
        return True
                


        