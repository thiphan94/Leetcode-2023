from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] == target:
                return True
            if matrix[i][-1] < target:
                continue
            if matrix[i][-1] > target:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == target:
                        return True
        return False
