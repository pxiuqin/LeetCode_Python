"""
 * https://leetcode.com/problems/valid-parentheses/
 * 20. 有效的括号
 * 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
 * 有效字符串需满足：
 * 左括号必须用相同类型的右括号闭合。
 * 左括号必须以正确的顺序闭合。
 *
 * 示例 1：
 * 输入：s = "()"
 * 输出：true
 * <p>
 * 示例2：
 * 输入：s = "()[]{}"
 * 输出：true
 * <p>
 * 示例3：
 * 输入：s = "(]"
 * 输出：false
 * <p>
 * 示例4：
 * 输入：s = "([)]"
 * 输出：false
 * <p>
 * 示例5：
 * 输入：s = "{[]}"
 * 输出：true
 * <p>
 * 提示：
 * 1 <= s.length <= 10^4
 * s 仅由括号 '()[]{}' 组成
"""


class Stack:
    def __init__(self):
        self._item = []

    def push(self, item):
        self._item.append(item)

    @property
    def size(self):
        return len(self._item)

    @property
    def is_empty(self):
        return len(self._item) == 0

    def pop(self):
        return self._item.pop()

    def peek(self):
        return self._item[-1]

    def print(self):
        print(self._item)


class ValidParentheses:
    def isValid(self, s):
        st = Stack()
        for i in range(len(s)):
            ch = s[i]
            if ch == '{' or ch == '[' or ch == '(':
                st.push(ch)
            elif ch == '}' or ch == ']' or ch == ')':
                if st.is_empty:
                    return False
                sch = st.peek()
                if (sch == '{' and ch == '}') or (sch == '[' and ch == ']') or (sch == '(' and ch == ')'):
                    st.pop()
                else:
                    return False
            else:
                return False

        return st.is_empty


def main():
    obj = ValidParentheses()
    print(obj.isValid("()"))
    print(obj.isValid("()[]{}"))
    print(obj.isValid("(]"))
    print(obj.isValid("([)]"))
    print(obj.isValid("{[]}"))


if __name__ == '__main__':
    main()
