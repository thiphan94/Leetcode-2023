from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # First pass: Identify zero rows and columns
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Second pass: Set the corresponding elements to zero
        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
