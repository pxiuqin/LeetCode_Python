"""
 * https://leetcode.com/problems/unique-paths-ii/
 * 63. 不同路径 II
 * 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
 * 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
 * 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
 * img(doc/img/0-100/UniquePaths.png)
 * 网格中的障碍物和空位置分别用 1 和 0 来表示。
 * <p>
 * 示例 1：
 * img(img/doc/UniquePathsII_1.jpg)
 * 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
 * 输出：2
 * 解释：
 * 3x3 网格的正中间有一个障碍物。
 * 从左上角到右下角一共有 2 条不同的路径：
 * 1. 向右 -> 向右 -> 向下 -> 向下
 * 2. 向下 -> 向下 -> 向右 -> 向右
 * <p>
 * 示例 2：
 * img(img/doc/UniquePathsII_2.jpg)
 * 输入：obstacleGrid = [[0,1],[0,0]]
 * 输出：1
 * <p>
 * 提示：
 * m ==obstacleGrid.length
 * n ==obstacleGrid[i].length
 * 1 <= m, n <= 100
 * obstacleGrid[i][j] 为 0 或 1
"""


class UniquePathsII:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        matrix = [[0 for c in range(n)] for r in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                matrix[i][0] = 1
            else:
                break  # if obstacle is stop current DOWN path

        for i in range(n):
            if obstacleGrid[0][i] != 1:
                matrix[0][i] = 1
            else:
                break  # if obstacle is stop current RIGHT path

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0   # if obstacle set 0
                else:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[m - 1][n - 1]


def main():
    obj = UniquePathsII()
    obstacle = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
    print(obj.uniquePathsWithObstacles(obstacle))
    print(obj.uniquePathsWithObstacles([[0, 1], [0, 0]]))


if __name__ == "__main__":
    main()
