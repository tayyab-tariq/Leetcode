class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows, cols, squares = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)

        # for row in range(len(board)):
        #     for col in range(len(board[row])):
        #         if board[row][col] != '.':
        #             if (board[row][col] in rows[row] or board[row][col] in cols[col] 
        #             or board[row][col] in squares[(row // 3, col // 3)]):
        #                 return False

        #             rows[row].add(board[row][col])
        #             cols[col].add(board[row][col])
        #             squares[(row // 3, col // 3)].add(board[row][col])
        
        # return True

        row, col, squares = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in squares[(i//3, j//3)]:
                    return False
                if board[i][j] != '.':
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    squares[(i//3, j//3)].add(board[i][j])
        return True
