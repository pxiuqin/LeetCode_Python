"""
* https://oj.leetcode.com/problems/regular-expression-matching/
 * 10. 正则表达式匹配
 * 给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。
 * '.' 匹配任意单个字符
 * '*' 匹配零个或多个前面的那一个元素
 * 所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。
 * <p>
 * 示例 1：
 * 输入：s = "aa" p = "a"
 * 输出：false
 * 解释："a" 无法匹配 "aa" 整个字符串。
 * <p>
 * 示例 2:
 * 输入：s = "aa" p = "a*"
 * 输出：true
 * 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
 * <p>
 * 示例3：
 * 输入：s = "ab" p = ".*"
 * 输出：true
 * 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
 * <p>
 * 示例 4：
 * 输入：s = "aab" p = "c*a*b"
 * 输出：true
 * 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
 * <p>
 * 示例 5：
 * 输入：s = "mississippi" p = "mis*is*p*."
 * 输出：false
 *
 * 提示：
 * 0 <= s.length<= 20
 * 0 <= p.length<= 30
 * s可能为空，且只包含从a-z的小写字母。
 * p可能为空，且只包含从a-z的小写字母，以及字符.和*。
 * 保证每次出现字符* 时，前面都匹配到有效的字符
 * <p>
 * <p>
 * Implement regular expression matching with support for '.' and '*'.
 * <p>
 * '.' Matches any single character.
 * '*' Matches zero or more of the preceding element.
 * Some examples:
 * isMatch("aa","a") → false
 * isMatch("aa","aa") → true
 * isMatch("aaa","aa") → false
 * isMatch("aa", "a*") → true
 * isMatch("aa", ".*") → true
 * isMatch("ab", ".*") → true
 * isMatch("aab", "c*a*b") → true
 * <p>
 * 大概思路如下：
 * - 若p为空，若s也为空，返回 true，反之返回 false。
 * - 若p的长度为1，若s长度也为1，且相同或是p为 '.' 则返回 true，反之返回 false。
 * - 若p的第二个字符不为*，若此时s为空返回 false，否则判断首字符是否匹配，且从各自的第二个字符开始调用递归函数匹配。
 * - 若p的第二个字符为*，进行下列循环，条件是若s不为空且首字符匹配（包括 p[0] 为点），调用递归函数匹配s和去掉前两个字符的p（这样做的原因是假设此时的星号的作用是让前面的字符出现0次，验证是否匹配），若匹配返回 true，否则s去掉首字母（因为此时首字母匹配了，我们可以去掉s的首字母，而p由于星号的作用，可以有任意个首字母，所以不需要去掉），继续进行循环。
 * - 返回调用递归函数匹配s和去掉前两个字符的p的结果（这么做的原因是处理星号无法匹配的内容，比如 s="ab", p="a*b"，直接进入 while 循环后，我们发现 "ab" 和 "b" 不匹配，所以s变成 "b"，那么此时跳出循环后，就到最后的 return 来比较 "b" 和 "b" 了，返回 true。再举个例子，比如 s="", p="a*"，由于s为空，不会进入任何的 if 和 while，只能到最后的 return 来比较了，返回 true，正确）。
 *
"""


class RegularExpressionMatching:
    def isMatch(self, s, p):
        # 若p为空，若s也为空，返回 true，反之返回 false。
        if p == "":
            return s == ""

        # 若p的长度为1，若s长度也为1，且相同或是p为 '.' 则返回 true，反之返回 false。
        if len(p) == 1:
            return len(s) == 1 and (p[0] == '.' or s[0] == p[0])

        # 若p的第二个字符不为*，若此时s为空返回 false，否则判断首字符是否匹配，且从各自的第二个字符开始调用递归函数匹配。
        if p[1] != '*':
            if s == "" or (p[0] != '.' and s[0] != p[0]):
                return False
            return self.isMatch(s[1:], p[1:])
        else:
            length = len(s)
            i = 0

            # 若p的第二个字符为*，进行下列循环，条件是若s不为空且首字符匹配（包括 p[0] 为点），调用递归函数匹配s和去掉前两个字符的p（这样做的原因是假设此时的星号的作用是让前面的字符出现0次，验证是否匹配），若匹配返回 true，否则s去掉首字母（因为此时首字母匹配了，我们可以去掉s的首字母，而p由于星号的作用，可以有任意个首字母，所以不需要去掉），继续进行循环。
            while i < length and (p[0] == '.' or p[0] == s[i]):
                if self.isMatch(s[i:], p[2:]):
                    return True
                i += 1

            return self.isMatch(s[i:], p[2:])


def main():
    obj = RegularExpressionMatching()
    print(obj.isMatch("", "a"))
    print(obj.isMatch("", "*"))
    print(obj.isMatch("a", ""))
    print(obj.isMatch("a", "*"))
    print(obj.isMatch("a", "."))
    print(obj.isMatch("aa", "."))
    print(obj.isMatch("aa", "a"))
    print(obj.isMatch("aa", "aa"))
    print(obj.isMatch("aarr", "aarr"))
    print(obj.isMatch("mississippi", "mis*is*p*."))
    print(obj.isMatch("aab", "c*a*b"))
    print(obj.isMatch("aab", "*a*b"))
    print(obj.isMatch("aab", ".a*b"))
    print(obj.isMatch("aab", "a*b"))


if __name__ == "__main__":
    main()
