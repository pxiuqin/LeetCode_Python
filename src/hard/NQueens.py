"""
 * https://leetcode.com/problems/n-queens/
 * The n-queens puzzle is the problem of placing n queens on an n×n chessboard
 * such that no two queens attack each other.
 * <p>
 * Given an integer n, return all distinct solutions to the n-queens puzzle.
 * <p>
 * Each solution contains a distinct board configuration of the n-queens' placement,
 * where 'Q' and '.' both indicate a queen and an empty space respectively.
 * <p>
 * For example,
 * There exist two distinct solutions to the 4-queens puzzle:
 * <p>
 * [
 * [".Q..",  // Solution 1
 * "...Q",
 * "Q...",
 * "..Q."],
 * <p>
 * ["..Q.",  // Solution 2
 * "Q...",
 * "...Q",
 * ".Q.."]
 * ]
 * <p>
 * 算法1
 * 这种棋盘类的题目一般是回溯法, 依次放置每行的皇后。在放置的时候，要保持当前的状态为合法，即当前放置位置的同一行、同一列、两条对角线上都不存在皇后。
 * <p>
 * 算法2
 * 用一个一位数组来存放当前皇后的状态。假设数组为int state[n], state[i]表示第 i 行皇后所在的列。那么在新的一行 k 放置一个皇后后:
 * 1) 判断列是否冲突，只需要看state数组中state[0…k-1] 是否有和state[k]相等；
 * 2) 判断对角线是否冲突：如果两个皇后在同一对角线，那么|row1-row2| = |column1 - column2|，（row1，column1），（row2，column2）分别为冲突的两个皇后的位置

"""


class NQueens:
    # 判断在cur[row][col]位置放一个皇后，是否是合法的状态
    # 已经保证了每行一个皇后，只需要判断列是否合法以及对角线是否合法。
    def isValid1(self, cur: list, row, col):
        # 列
        for i in range(row):
            if cur[i][col] == 'Q':
                return False

        i = row - 1
        j = col - 1
        # 右对角线(只需要判断对角线上半部分，因为后面的行还没有开始放置)
        while i >= 0 and j >= 0:
            if cur[i][j] == 'Q':
                return False

            i -= 1
            j -= 1

        i = row - 1
        j = col + 1
        # 左对角线(只需要判断对角线上半部分，因为后面的行还没有开始放置)
        while i >= 0 and j < len(cur):
            if cur[i][j] == 'Q':
                return False

            i -= 1
            j += 1

        return True

    def helper(self, cur: list, row, result: list):
        if row == len(cur):
            result.append(cur[:])

        for i in range(len(cur)):
            if self.isValid1(cur, row, i):
                cur[row][i] = 'Q'
                self.helper(cur, row + 1, result)
                cur[row][i] = '.'

    def solveNQueens(self, n):
        result = []

        s = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append('.')

            s.append(temp[:])

        self.helper(s, 0, result)

        return result


def main():
    obj = NQueens()
    print(obj.solveNQueens(4))
    print(obj.solveNQueens(8))


if __name__ == '__main__':
    main()
