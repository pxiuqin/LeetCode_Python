"""
 * https://oj.leetcode.com/problems/longest-palindromic-substring/
 * 5. 最长回文子串
 * 给你一个字符串 s，找到 s 中最长的回文子串。
 * <p>
 * 示例 1：
 * 输入：s = "babad"
 * 输出："bab"
 * 解释："aba" 同样是符合题意的答案。
 * <p>
 * 示例 2：
 * 输入：s = "cbbd"
 * 输出："bb"
 * <p>
 * 示例 3：
 * 输入：s = "a"
 * 输出："a"
 * <p>
 * 示例 4：
 * 输入：s = "ac"
 * 输出："a"
 *  
 * <p>
 * 提示：
 * <p>
 * 1 <= s.length <= 1000
 * s 仅由数字和英文字母（大写和/或小写）组成
"""

from turtle import st


class LongestPalindromicSubstring:
    def isPalindrome(self, s):
        n = len(s)
        for i in range(n):
            if s[i] != s[n - i - 1]:
                return False

        return True

    def longestPalindrome1(self, s):
        n = len(s)
        longest = ""
        for i in range(n):
            for j in range(i + 1, n):
                str = s[i:j + 1]
                if self.isPalindrome(str):
                    longest = str
            if len(longest) == 0:
                longest = s[0]

        return longest

    def findPalindrome(self, s, left, right):
        n = len(s)
        while left >= 0 and right <= n - 1 and s[left] == s[right]:
            left -= 1
            right += 1

        if left + 1 <= right:
            return s[left + 1:right]
        else:
            return ""

    def longestPalindrome_recursive_way(self, s):
        n = len(s)
        if n <= 1:
            return s

        longest = ""
        for i in range(n - 1):
            # handler 'abba'
            str = self.findPalindrome(s, i, i)
            if (len(str) > len(longest)):
                longest = str

            # handler 'abcba'
            str = self.findPalindrome(s, i, i + 1)
            if len(str) > len(longest):
                longest = str

        return longest

    def longestPalindrome3(self, s):
        longest = ""
        n = len(s)
        if n <= 1:
            return s

        matrix = [[False for i in range(n)] for i in range(n)]
        for i in reversed(range(n)):
            for j in range(i, n):
                # j - i < 2 is 'bb' or matrix[i + 1][j - 1] is 'bab'
                if i == j or (s[i] == s[j] and (j - i < 2 or matrix[i + 1][j - 1])):
                    matrix[i][j] = True
                    if len(longest) < j - i + 1:
                        longest = s[i:j + 1]

        return longest

    def longestPalindrome4(self, s):
        n = len(s)
        if n <= 1:
            return s

        start = 0
        longest = 0
        matrix = [[False] * n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = True
            for j in range(i+1):
                if i == j or (s[i]==s[j] and (i-j < 2 or matrix[i-1][j+1])):
                    matrix[i][j] = True
                    if longest < i-j+1:
                        longest = i-j+1
                        start = j

        return s[start:longest+1]


def main():
    obj = LongestPalindromicSubstring()
    print(obj.longestPalindrome4("bbabad"))
    print(obj.longestPalindrome3("bbabad"))
    print(obj.longestPalindrome3("bbbbad"))
    print(obj.longestPalindrome3("cbbd"))
    print(obj.longestPalindrome1("a"))
    print(obj.longestPalindrome1("ac"))

    print(obj.longestPalindrome_recursive_way("bbabad"))
    print(obj.longestPalindrome_recursive_way("bbbbad"))


if __name__ == "__main__":
    main()
