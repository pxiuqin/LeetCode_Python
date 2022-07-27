"""
* https://leetcode.com/problems/minimum-window-substring/
 * 76. 最小覆盖子串
 * 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
 *
 * 注意：
 * 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
 * 如果 s 中存在这样的子串，我们保证它是唯一的答案。
 *
 * 示例 1：
 * 输入：s = "ADOBECODEBANC", t = "ABC"
 * 输出："BANC"

 * 示例 2：
 * 输入：s = "a", t = "a"
 * 输出："a"

 * 示例 3:
 * 输入: s = "a", t = "aa"
 * 输出: ""
 * 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
 * 因此没有符合条件的子字符串，返回空字符串。
 *
 * 提示：
 * 1 <= s.length, t.length <= 105
 * s 和 t 由英文字母组成
 *
 * 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
 *
 * <p>
 * Given a string S and a string T, find the minimum window in S which will
 * contain all the characters in T in complexity O(n).
 * <p>
 * For example,
 * S = "ADOBECODEBANC"
 * T = "ABC"
 * <p>
 * Minimum window is "BANC".
 * <p>
 * Note:
 * <p>
 * > If there is no such window in S that covers all characters in T,
 * return the emtpy string "".
 * <p>
 * > If there are multiple such windows, you are guaranteed that there
 * will always be only one unique minimum window in S.
 * 解题思路其实就是通过双指针维持一个Window，窗口右指针向右扩张用来找到包含子串为目的，窗口左指针向右收缩以使子串最小。
 * 典型的滑动窗口方法的实现。
"""
import sys

MAX_CHARS = 256  # Declare two "hash map" for ASCII chars
NOT_EXISTED = -1
NOT_FOUND = 0


class MinimumWindowSubstring:
    def minWindow(self, s, t):
        win = ""
        if len(s) <= 0 or len(t) <= 0 or len(t) > len(s):
            return win

        window = [NOT_EXISTED for i in range(MAX_CHARS)]  # represents the char found in string S
        dict = [NOT_EXISTED for i in range(MAX_CHARS)]  # stores the chars in string T

        # init t for dict and window
        for i in range(len(t)):
            index = ord(t[i])
            if dict[index] == NOT_EXISTED:
                dict[index] = 1
            else:
                dict[index] += 1

            window[index] = NOT_FOUND

        start = -1
        win_size = sys.maxsize
        letter_fount = 0
        left = 0

        for right in range(len(s)):
            chri = ord(s[right])

            if dict[chri] == NOT_EXISTED:
                continue

            # if s[i] is existed in t
            window[chri] += 1

            # if one char has been found enough times, then do not do letter_found++
            if window[chri] <= dict[chri]:
                letter_fount += 1

            if letter_fount >= len(t):
                # Find the left of the window , try to make the window smaller
                # 1) windows[S[left]] == NOT_EXISTED  ===> the char at the `left` is not in T
                # 2) window[S[left]] > dict[S[left]]   ===> a same char appeared more than excepted.
                chli = ord(s[left])
                while window[chli] == NOT_EXISTED or window[chli] > dict[chli]:
                    if dict[chli] != NOT_EXISTED:
                        # move the left of window
                        window[chli] -= 1

                        # reduce the number of letters found
                        if window[chli] < dict[chli]:
                            letter_fount -= 1
                    left += 1
                    chli = ord(s[left])

                # Calculate the minimized window size
                if win_size > right - left + 1:
                    start = left
                    win_size = right - left + 1

        if start >= 0 and win_size > 0:
            win = s[start:start + win_size]

        return win


def main():
    obj = MinimumWindowSubstring()
    print(obj.minWindow("ADOBECODEBANC", "ABC"))


if __name__ == "__main__":
    main()
