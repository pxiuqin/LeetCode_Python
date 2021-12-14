"""
 * https://leetcode.com/problems/search-a-2d-matrix/
 * 74. 搜索二维矩阵
 * 编写一个高效的算法来判断m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：
 * 每行中的整数从左到右按升序排列。
 * 每行的第一个整数大于前一行的最后一个整数。
 * <p>
 * 示例 1：
 * img(doc/img/0-100/mat.jpg)
 * 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
 * 输出：true
 * <p>
 * 示例 2：
 * img(img/doc/mat2.jpg)
 * 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
 * 输出：false
 * <p>
 * 提示：
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 100
 * -10^4 <= matrix[i][j], target <= 10^4
"""


class SearchA2DMatrix:
    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) == 0 or matrix[0] is None or len(matrix[0]) == 0:
            return False

        matrix
        rows = len(matrix)
        cols = len(matrix[0])

        start = 0
        end = rows * cols - 1  # matrix as one list

        while start + 1 < end:
            mid = (start + end) // 2
            mid_value = matrix[mid // cols][mid % cols]
            if mid_value == target:
                return True
            elif mid_value < target:
                start = mid
            else:
                end = mid

        if matrix[start // cols][start % cols] == target:
            return True

        if matrix[end // cols][end % cols] == target:
            return True

        return False


def main():
    obj = SearchA2DMatrix()
    print(obj.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(obj.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))


if __name__ == "__main__":
    main()
