"""
 * https://leetcode.com/problems/length-of-last-word/
 * 58. 最后一个单词的长度
 * 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
 * <p>
 * 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
 * <p>
 * 示例 1：
 * 输入：s = "Hello World"
 * 输出：5
 * <p>
 * 示例 2：
 * 输入：s = "   fly me   to   the moon  "
 * 输出：4
 * <p>
 * 示例 3：
 * 输入：s = "luffy is still joyboy"
 * 输出：6
 * <p>
 * 提示：
 * 1 <= s.length <= 10^4
 * s 仅有英文字母和空格 ' ' 组成
 * s 中至少存在一个单词
"""


class LengthOfLastWord:
    def lenthOfLastWord(self, s):
        # don't forget rangeCheck
        if s is None or len(s) == 0:
            return 0

        size = len(s)
        i = size - 1
        while i >= 0 and s[i] == ' ':
            i -= 1

        if i == -1:
            return 0

        count = 0
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count


def main():
    obj = LengthOfLastWord()
    print(obj.lenthOfLastWord("Hello World"))
    print(obj.lenthOfLastWord("   fly me   to   the moon  "))
    print(obj.lenthOfLastWord("luffy is still joyboy"))


if __name__ == "__main__":
    main()
