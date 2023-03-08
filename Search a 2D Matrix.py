class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, col = len(matrix), len(matrix[0])

        top , bot = 0, rows - 1

        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][0] > target:
                bot = row - 1
            elif  matrix[row][-1] < target:
                top = row + 1            
            else:
                break

        if top > bot:
            return False 

        left, right = 0, col - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True        
        return False
