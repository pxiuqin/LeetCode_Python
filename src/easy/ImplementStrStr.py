"""
 * https://leetcode.com/problems/implement-strstr/
 * 28. 实现 strStr()
 * <p>
 * 实现strStr()函数。
 * 给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。
 * <p>
 * 说明：
 * 当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
 * 对于本题而言，当needle是空字符串时我们应当返回 0 。这与 C 语言的strstr()以及 Java 的indexOf()定义相符。
 * <p>
 * 示例 1：
 * 输入：haystack = "hello", needle = "ll"
 * 输出：2
 * <p>
 * 示例 2：
 * 输入：haystack = "aaaaa", needle = "bba"
 * 输出：-1
 * <p>
 * 示例 3：
 * 输入：haystack = "", needle = ""
 * 输出：0
 * <p>
 * 提示：
 * 0 <= haystack.length, needle.length <= 5 * 10^4
 * haystack 和 needle 仅由小写英文字符组成
"""


class ImplementStrStr:
    def strStr(self, haystack, needle):
        if haystack is None or needle is None:
            return -1

        if len(needle) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle):
                if haystack[i + j] != needle[j]:
                    break;
                j += 1

            if j == len(needle):
                return i

        return -1


def main():
    obj = ImplementStrStr()
    print(obj.strStr("hello", "ll"))
    print(obj.strStr("aaaaa", "bba"))
    print(obj.strStr("", ""))


if __name__ == '__main__':
    main()
