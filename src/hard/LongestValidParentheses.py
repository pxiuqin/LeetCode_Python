"""
 * https://leetcode.com/problems/longest-valid-parentheses/
 * <p>
 * 32. 最长有效括号
 * 给你一个只包含 '('和 ')'的字符串，找出最长有效（格式正确且连续）括号子串的长度。
 * <p>
 * 示例 1：
 * 输入：s = "(()"
 * 输出：2
 * 解释：最长有效括号子串是 "()"
 * <p>
 * 示例 2：
 * 输入：s = ")()())"
 * 输出：4
 * 解释：最长有效括号子串是 "()()"
 * <p>
 * 示例 3：
 * 输入：s = ""
 * 输出：0
 * <p>
 * 提示：
 * 0 <= s.length <= 3 * 10^4
 * s[i] 为 '(' 或 ')'
"""


class LongestValidParentheses:
    def longestValidParentheses(self, s):
        maxLen = 0
        lastError = -1

        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                    size = i - lastError if len(stack) == 0 else i - stack[len(stack) - 1]

                    if size > maxLen:
                        maxLen = size
                else:
                    lastError = i

        return maxLen


def main():
    obj = LongestValidParentheses()
    print(obj.longestValidParentheses("(()"))
    print(obj.longestValidParentheses(")()())"))


if __name__ == '__main__':
    main()
