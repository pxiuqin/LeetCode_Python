"""
 * https://leetcode.com/problems/spiral-matrix-ii/
 59. 螺旋矩阵 II
 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix
 示例 1：doc/img/0-100/spiraln.jpg
 输入：n = 3
 输出：[[1,2,3],[8,9,4],[7,6,5]]

 示例 2：
 输入：n = 1
 输出：[[1]]
 * <p>
 * Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
 * <p>
 * For example,
 * Given n = 3,
 * <p>
 * You should return the following matrix:
 * <p>
 * [
 * [ 1, 2, 3 ],
 * [ 8, 9, 4 ],
 * [ 7, 6, 5 ]
 * ]
"""


class SpiralMatrixII:
    def generateMatrix(self, n, m):
        matrix = []
        if n <= 0:
            return matrix

        matrix = [[0 for j in range(m)] for i in range(n)]

        row = n
        col = m
        cnt = 1
        for r, c in zip(range((row + 1) // 2), range((col + 1) // 2)):
            # top
            for i in range(c, col - c):
                matrix[r][i] = cnt
                cnt += 1

            # right
            for i in range(r + 1, row - r):
                matrix[i][col - c - 1] = cnt
                cnt += 1

            # bottom
            for i in range(col - c - 2, c - 1, -1):
                if row - r - 1 > r:
                    matrix[row - r - 1][i] = cnt
                    cnt += 1
                else:
                    break

            # left
            for i in range(row - r - 2, r, -1):
                if col - c - 1 > c:
                    matrix[i][c] = cnt
                    cnt += 1
                else:
                    break

        return matrix


def main():
    obj = SpiralMatrixII()
    print(obj.generateMatrix(3, 3))
    print(obj.generateMatrix(4, 4))


if __name__ == "__main__":
    main()
