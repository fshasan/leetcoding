class Solution(object):
    def diagonalSum(self, mat):
        sum = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j or j == len(mat) - i - 1:
                    sum += mat[i][j]
        return sum
