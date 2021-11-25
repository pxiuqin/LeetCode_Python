"""
 * https://leetcode.com/problems/n-queens-ii/
 * 52. N皇后 II
 * n皇后问题研究的是如何将n个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
 * <p>
 * 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
 * <p>
 * 示例 1：
 * img(doc/img/0-100/queens2.jpg)
 * 输入：n = 4
 * 输出：2
 * 解释：如上图所示，4 皇后问题存在两个不同的解法。
 * <p>
 * 示例 2：
 * 输入：n = 1
 * 输出：1
 * <p>
 * 提示：
 * 1 <= n <= 9
 * 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
"""


class NQueensII:
    def isValid(self, attemptedColumn, attemptedRow, queenInColumn: list):
        for i in range(attemptedRow):
            if attemptedColumn == queenInColumn[i] or abs(attemptedColumn - queenInColumn[i]) == abs(attemptedRow - i):
                return False

        return True

    # the solution is same as the "N Queens" problem.
    def solveNQueenRecursive(self, n, currentRow, solution: list):
        count = 0

        for i in range(n):
            if self.isValid(i, currentRow, solution):
                if currentRow + 1 == n:
                    count += 1
                    continue
                solution[currentRow] = i
                count += self.solveNQueenRecursive(n, currentRow + 1, solution)

        return count

    def totalNQueens(self, n):
        solution = [0 for i in range(n)]
        result = self.solveNQueenRecursive(n, 0, solution)

        return result


def main():
    obj = NQueensII()
    print(obj.totalNQueens(4))
    print(obj.totalNQueens(8))


if __name__ == '__main__':
    main()
