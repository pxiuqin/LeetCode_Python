"""
 * https://leetcode.com/problems/minimum-path-sum/
 * 64.最小路径和
 * 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
 * 说明：每次只能向下或者向右移动一步。
 *
 * 示例:
 * 输入:
 * [
 *   [1,3,1],
 *   [1,5,1],
 *   [4,2,1]
 * ]
 * 输出: 7
 * 解释: 因为路径 1→3→1→1→1 的总和最小。

 * Given a m x n grid filled with non-negative numbers, find a path from top left to
 * bottom right which minimizes the sum of all numbers along its path.
 *
 * Note: You can only move either down or right at any point in time.
 *
 * 思路：采用动态规划的思路，维护一个二维数组dp，其中dp[i][j]表示在[i,j]节点的最小路径，因为只能向下和向右，所以[i,j]节点只能由[i-1,j]和[i,j-1]过来，取其中较小的即可，及递推公式如下所示：
 * dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1]);
"""


class MinimumPathSum:
    def minPathSum(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        matrix = [[0 for c in range(n)] for r in range(m)]

        matrix[0][0] = grid[0][0]
        for i in range(1, m):
            matrix[i][0] = grid[i][0] + matrix[i - 1][0]

        for i in range(1, n):
            matrix[0][i] = grid[0][i] + matrix[0][i - 1]

        for i in range(1, m):
            for j in range(1, n):
                # add current value and minimum cumulative sum
                matrix[i][j] = grid[i][j] + min(matrix[i - 1][j], matrix[i][j - 1])

        return matrix[m - 1][n - 1]


def main():
    obj = MinimumPathSum()
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    print(obj.minPathSum(grid))


if __name__ == "__main__":
    main()
