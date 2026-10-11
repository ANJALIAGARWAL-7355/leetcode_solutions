
class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        # Find all positions containing 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Set the corresponding rows to zero
        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
