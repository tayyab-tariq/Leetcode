class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1

        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else: 
                break

        left, right = 0, len(matrix[row])-1
        while left <= right:
            col = (left + right) // 2
            if matrix[row][col] > target:
                right = col - 1
            elif matrix[row][col] < target:
                left = col + 1
            else: 
                return True  
        return False
