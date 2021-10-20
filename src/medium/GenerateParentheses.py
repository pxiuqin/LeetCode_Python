"""
 * https://leetcode.com/problems/generate-parentheses/
 * 22. 括号生成
 * 数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。
 * <p>
 * 示例 1：
 * 输入：n = 3
 * 输出：["((()))","(()())","(())()","()(())","()()()"]
 * <p>
 * 示例 2：
 * 输入：n = 1
 * 输出：["()"]
 *
 * 提示：
 * 1 <= n <= 8
 * <p>
 * 思路：
 * 这道题可以用回溯法解决，即穷举出所有可能，再按照规则过滤结果。但是更好的办法是在回溯的过程中，就进行规则的判断，进行剪枝操作：
 * 只有在我们知道序列仍然保持有效时才添加 '(' or ')'，我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，
 * 如果我们还剩一个位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号。
"""


class GenerateParentheses:
    def generator(self, result: list, left, right, s):
        if left == 0 and right == 0:
            result.append(s)
            return
        if left > 0:
            self.generator(result, left - 1, right, s + '(')
        if right > 0 and right > left:
            self.generator(result, left, right - 1, s + ')')

    def generateParenthesis(self, n):
        result = []
        self.generator(result, n, n, "")
        return result


def main():
    obj = GenerateParentheses()
    print(obj.generateParenthesis(3))
    print(obj.generateParenthesis(1))


if __name__ == '__main__':
    main()
