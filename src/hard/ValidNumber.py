"""
 * https://leetcode.com/problems/valid-number/
 * 65. 有效数字
 * 有效数字（按顺序）可以分成以下几个部分：
 *
 * 一个 小数 或者 整数
 * （可选）一个 'e' 或 'E' ，后面跟着一个 整数
 * 小数（按顺序）可以分成以下几个部分：
 *
 * （可选）一个符号字符（'+' 或 '-'）
 * 下述格式之一：
 * 至少一位数字，后面跟着一个点 '.'
 * 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
 * 一个点 '.' ，后面跟着至少一位数字
 * 整数（按顺序）可以分成以下几个部分：
 *
 * （可选）一个符号字符（'+' 或 '-'）
 * 至少一位数字
 * 部分有效数字列举如下：
 *
 * ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
 * 部分无效数字列举如下：
 *
 * ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
 * 给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
 *
 * 示例 1：
 * 输入：s = "0"
 * 输出：true
 *
 * 示例 2：
 * 输入：s = "e"
 * 输出：false

 * 示例 3：
 * 输入：s = "."
 * 输出：false

 * 示例 4：
 * 输入：s = ".1"
 * 输出：true
 *
 * 提示：
 *
 * 1 <= s.length <= 20
 * s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。
"""


class ValidNumber:
    def is_digit(self, c):
        return c >= '0' and c <= '9'

    def is_space(self, c):
        return c == ' ' or c == '\t' or c == '\n' or c == '\r' or c == '\f'

    def is_number(self, s):
        point = False
        hasE = False

        # trim the space
        while len(s) > 0 and self.is_space(s[0]):
            s = s[1:]

        # check empty
        if len(s) == 0:
            return False

        # check empty
        if s[0] == '+' or s[0] == '-':
            s = s[1:]

        i = 0
        while i < len(s):
            # if contain '.'
            if s[i] == '.':
                if hasE is True or point is True:
                    return False

                index = i + 1
                if index < len(s) and not self.is_digit(s[index]):
                    return False
                point = True

                i += 1
                continue

            # if contain 'e'
            if s[i] == 'e':
                if hasE is True:
                    return False

                index = i + 1
                i += 1
                if i < len(s) and (s[i] == '+' or s[i] == '-'):
                    index = i + 1

                if index < len(s):
                    if not self.is_digit(s[index]):
                        return False
                else:
                    return False

                hasE = True

                i += 1
                continue

            # if contain space, check the rest chars are space or not
            if self.is_space(s[i]):
                return False

            if not self.is_digit(s[i]):
                return False

            i += 1

        return True


def main():
    obj = ValidNumber()
    print("1.044 is %s" % obj.is_number("1.044"))
    print(" 1.044 is %s" % obj.is_number(" 1.044"))
    print(" 1.044  is %s" % obj.is_number(" 1.044 "))
    print("1.a is %s" % obj.is_number("1.a"))
    print("abc is %s" % obj.is_number("abc"))
    print("e is %s" % obj.is_number("e"))
    print("1e is %s" % obj.is_number("1e"))
    print("1e2 is %s" % obj.is_number("1e2"))
    print("'' is %s" % obj.is_number(""))
    print("' ' is %s" % obj.is_number(" "))
    print("1. is %s" % obj.is_number("1."))
    print(".2 is %s" % obj.is_number(".2"))
    print(" . is %s" % obj.is_number(" . "))
    print(".is %s" % obj.is_number("."))
    print("1.2.3 is %s" % obj.is_number("1.2.3"))
    print("1e2e3 is %s" % obj.is_number("1e2e3"))
    print("1.. is %s" % obj.is_number("1.."))
    print("+1. is %s" % obj.is_number("+1."))
    print("-1. is %s" % obj.is_number(" -1."))
    print("6e6.5 is %s" % obj.is_number("6e6.5"))
    print("005047e+6 is %s" % obj.is_number("005047e+6"))
    print("5047e+6 is %s" % obj.is_number("5047e-6"))


if __name__ == "__main__":
    main()
