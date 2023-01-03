class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_rows = len(board)
        if num_rows != 9:
            return False
        
        row = [[] for i in range(len(board))]
        col = [[] for i in range(len(board))]
        sqr = collections.defaultdict(list)
        
        
        for i in range(num_rows):
            if len(board[i]) != 9:
                return False

            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in sqr[(i//3,j//3)]:
                        return False
                    
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])                    
                    sqr[(i//3,j//3)].append(board[i][j])
        
        return True
