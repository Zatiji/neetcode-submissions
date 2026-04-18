class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # First, we check the head of each column using binary search
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            row = top + (bottom - top) // 2

            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else :
                break
        
        if not top <= bottom:
            return False

        print(row)
        # Second, we do binary search inside the row
        row_vec = matrix[row]
        l = 0
        r = len(row_vec) - 1

        while l <= r:
            m = l + (r-l) // 2

            if target > row_vec[m]:
                l = m + 1
            elif target <row_vec[m]:
                r = m - 1
            else:
                return True

        return False

        
        
            
        