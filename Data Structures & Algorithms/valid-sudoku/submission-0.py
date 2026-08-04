class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):

            valid_col = [board[i][j] for j in range(len(board[i])) if board[i][j] != "."]
            if len(set(valid_col)) != len(valid_col):
                return False

            valid_row = [board[j][i] for j in range(len(board[i])) if board[j][i] != "."]
            if len(set(valid_row)) != len(valid_row):
                return False

        for i,j in [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]:
            sub_grid = []
            for i_start in range(i,i+3):
                for j_start in range(j,j+3):
                    value = board[i_start][j_start]
                    if value != ".":
                        sub_grid.append(value)
            if len(set(sub_grid)) != len(sub_grid):
                return False
        
        return True
                
