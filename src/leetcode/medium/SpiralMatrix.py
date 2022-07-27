"""
 * https://leetcode.com/problems/spiral-matrix/
 * 54. 螺旋矩阵
 * 给你一个 m 行 n 列的矩阵matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
 * <p>
 * 示例 1：
 * img(doc/img/spiral1.jpg)
 * 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[1,2,3,6,9,8,7,4,5]
 * <p>
 * 示例 2：
 * img(doc/img/spiral.jpg
 * 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 * 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 * <p>
 * 提示：
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 10
 * -100 <= matrix[i][j] <= 100
"""


class SpiralMatrix:
    def spiralOrder(self, matrix):
        v = []
        row = len(matrix)
        if row <= 0:
            return v

        col = len(matrix[0])
        if col <= 0:
            return v

        for r, c in zip(range((row + 1) // 2), range((col + 1) // 2)):
            # top
            for i in range(c, col - c):
                v.append(matrix[r][i])

            # right
            for i in range(r + 1, row - r):
                v.append(matrix[i][col - c - 1])

            # bottom
            for i in range(col - c - 2, c - 1, -1):
                if row - r - 1 > r:
                    v.append(matrix[row - r - 1][i])

            # left
            for i in range(row - r - 2, r, -1):
                if col - c - 1 > c:
                    v.append(matrix[i][c])

        return v


def main():
    obj = SpiralMatrix()
    print(obj.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(obj.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))


if __name__ == "__main__":
    main()
