"""
48. 旋转图像
* https://leetcode.com/problems/rotate-image/
 * <p>
 * Example 1:
 * img:doc/img/0-100/mat1.jpg
 * Given input matrix =
 * [
 * [1,2,3],
 * [4,5,6],
 * [7,8,9]
 * ],
 * <p>
 * rotate the input matrix in-place such that it becomes:
 * [
 * [7,4,1],
 * [8,5,2],
 * [9,6,3]
 * ]
 * <p>
 * Example 2:
 * img:doc/img/0-100/mat1_2 .jpg
 * Given input matrix =
 * [
 * [ 5, 1, 9,11],
 * [ 2, 4, 8,10],
 * [13, 3, 6, 7],
 * [15,14,12,16]
 * ],
 * <p>
 * rotate the input matrix in-place such that it becomes:
 * [
 * [15,13, 2, 5],
 * [14, 3, 4, 1],
 * [12, 6, 8, 9],
 * [16, 7,10,11]
 * ]
 * <p>
 * 一个n x n的二维矩阵表示一个图像，将图像顺时针旋转90度。要求in-place，所以就不能用额外的空间了。
 * <p>
 * 解法1: 先以对角线为轴翻转得到其转置矩阵，再以中间竖轴翻转。
 * 1  2  3　　　 　1  4  7　　　　  7  4  1
 * 4  5  6　-->　  2  5  8　 -->    8  5  2
 * 7  8  9 　　　  3  6  9　　   　 9  6  3
 * <p>
 * 解法2: 先以反对角线翻转，再以中间水平轴翻转。
 * 1  2  3　　　  9  6  3　　　　  7  4  1
 * 4  5  6　-->　 8  5  2　 -->    8  5  2
 * 7  8  9 　　　 7  4  1　　　　  9  6  3
 */
"""


class RotateImage:
    # rotate clockwise
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n // 2):
            low = i
            high = n - i - 1

            for j in range(low, high):
                tmp = matrix[i][j]

                # left to top
                matrix[i][j] = matrix[n - j - 1][i]

                # bottom to left
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]

                # right to bottom
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]

                # top to right
                matrix[j][n - i - 1] = tmp

        return matrix

    def rotate1(self, matrix):
        n = len(matrix)

        # 先以对角线为轴翻转得到其转置矩阵
        for i in range(n):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # 中间竖轴翻转
        for i in range(n):
            for j in range(n // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = temp

        return matrix

    def rotate2(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(n - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][n - i - 1]
                matrix[n - j - 1][n - i - 1] = temp

        for j in range(n):
            for i in range(n // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - i - 1][j]
                matrix[n - i - 1][j] = temp

        return matrix


def main():
    obj = RotateImage()
    print(obj.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(obj.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))

    print()
    print(obj.rotate1([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(obj.rotate1([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))

    print()
    print(obj.rotate2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(obj.rotate2([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))


if __name__ == '__main__':
    main()
