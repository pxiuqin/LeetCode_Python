"""
 * https://leetcode.com/problems/sudoku-solver/
 * 37. 解数独
 * 编写一个程序，通过填充空格来解决数独问题。
 * <p>
 * 数独的解法需 遵循如下规则：
 * <p>
 * 数字1-9在每一行只能出现一次。
 * 数字1-9在每一列只能出现一次。
 * 数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
 * 数独部分空格内已填入了数字，空白格用'.'表示。
 * <p>
 * 示例：
 * (img:doc/img/sudoku-by-9.png)
 * <p>
 * 输入：board = [
 * ["5","3",".",".","7",".",".",".","."],
 * ["6",".",".","1","9","5",".",".","."],
 * [".","9","8",".",".",".",".","6","."],
 * ["8",".",".",".","6",".",".",".","3"],
 * ["4",".",".","8",".","3",".",".","1"],
 * ["7",".",".",".","2",".",".",".","6"],
 * [".","6",".",".",".",".","2","8","."],
 * [".",".",".","4","1","9",".",".","5"],
 * [".",".",".",".","8",".",".","7","9"]]
 * <p>
 * 输出：[
 * ["5","3","4","6","7","8","9","1","2"],
 * ["6","7","2","1","9","5","3","4","8"],
 * ["1","9","8","3","4","2","5","6","7"],
 * ["8","5","9","7","6","1","4","2","3"],
 * ["4","2","6","8","5","3","7","9","1"],
 * ["7","1","3","9","2","4","8","5","6"],
 * ["9","6","1","5","3","7","2","8","4"],
 * ["2","8","7","4","1","9","6","3","5"],
 * ["3","4","5","2","8","6","1","7","9"]]
 * 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
 * (img:doc/img/0-100/sudoku-by-9-solutionsvg.png)
"""


class SudokuSolver:
    def __init__(self):
        self.cnt = 9
        self.row_mask = None
        self.col_mask = None
        self.area_mask = None

    def initSudokuMask(self, board):
        self.row_mask = [[False for i in range(self.cnt)] for j in range(self.cnt)]
        self.col_mask = [[False for i in range(self.cnt)] for j in range(self.cnt)]
        self.area_mask = [[False for i in range(self.cnt)] for j in range(self.cnt)]

        # check the rows and cols
        for r in range(len(board)):
            for c in range(len(board[r])):
                if str.isdigit(board[r][c]) is False:
                    continue

                idx = ord(board[r][c]) - ord('0') - 1

                # check the rows/cols/ares
                area = (r // 3) * 3 + (c // 3)
                if self.row_mask[r][idx] or self.col_mask[c][idx] or self.area_mask[area][idx]:
                    return False

                self.row_mask[r][idx] = self.col_mask[c][idx] = self.area_mask[area][idx] = True

        return True

    def recursiveSudoKu(self, board, row, col):
        if row >= self.cnt:
            return True

        if col >= self.cnt:
            # recursive next row when column equal 9
            return self.recursiveSudoKu(board, row + 1, 0)

        if board[row][col] != '.':
            # recursive next column
            return self.recursiveSudoKu(board, row, col + 1)

        # pick a number for empty cell
        for i in range(self.cnt):
            area = (row // 3) * 3 + (col // 3)
            if self.row_mask[row][i] or self.col_mask[col][i] or self.area_mask[area][i]:
                continue

            # set the number and solve it recursively
            board[row][col] = str(i + 1)
            self.row_mask[row][i] = self.col_mask[col][i] = self.area_mask[area][i] = True

            if self.recursiveSudoKu(board, row, col + 1) is True:
                return True  # recursive each columns
            else:
                board[row][col] = '.'  # 把后边儿的“.“改成数字后，发现做不下去了，得回溯，把这个数字改回.
                self.row_mask[row][i] = self.col_mask[col][i] = self.area_mask[area][i] = False

        return False

    def solveSudoku(self, board):
        if self.initSudokuMask(board) is False:
            return False

        return self.recursiveSudoKu(board, 0, 0)


def main():
    obj = SudokuSolver()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    obj.solveSudoku(board)
    print(board)


if __name__ == '__main__':
    main()
