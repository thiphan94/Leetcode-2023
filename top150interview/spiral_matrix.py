from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix[0])
        n = len(matrix)
        res = []
        if m == 0 or n == 0:
            return res
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        step = 0
        while l <= r and t <= b:
            if step % 4 == 0:
                for i in range(l, r + 1):
                    res.append(matrix[t][i])
                t += 1
            if step % 4 == 1:
                for i in range(t, b + 1):
                    res.append(matrix[i][r])
                r -= 1
            if step % 4 == 2:
                for i in range(r, l - 1, -1):
                    res.append(matrix[b][i])
                b -= 1
            if step % 4 == 3:
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                l += 1
            step += 1
        return res
