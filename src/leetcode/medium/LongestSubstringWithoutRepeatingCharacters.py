"""
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * 3. 无重复字符的最长子串
 * 给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。
 *
 * 示例1:
 * 输入: s = "abcabcbb"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

 * 示例 2:
 * 输入: s = "bbbbb"
 * 输出: 1
 * 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

 * 示例 3:
 * 输入: s = "pwwkew"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
 *     请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。

 * 示例 4:
 * 输入: s = ""
 * 输出: 0
 *
 * 提示：
 * 0 <= s.length <= 5 * 10^4
 * s由英文字母、数字、符号和空格组成
 * 介绍一种线性的算法，也是这类题目最常见的方法。
 * 基本思路是维护一个窗口，每次关注窗口中的字符串，在每次判断中，左窗口和右窗口选择其一向前移动。
 * 同样是维护一个HashSet, 正常情况下移动右窗口，如果没有出现重复则继续移动右窗口，
 * 如果发现重复字符，则说明当前窗口中的串已经不满足要求，继续移动右窗口不可能得到更好的结果，
 * 此时移动左窗口，直到不再有重复字符为止，中间跳过的这些串中不会有更好的结果，
 * 因为他们不是重复就是更短。因为左窗口和右窗口都只向前，所以两个窗口都对每个元素访问不超过一遍，
 * 因此时间复杂度为O(2*n)=O(n),是线性算法。
 * 空间复杂度为HashSet的size,也是O(n).
"""


class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s):
        if s is None or len(s) == 0:
            return 0

        tempSet = set()
        maxValue = 0
        walker = 0  # left windows
        runner = 0  # right windows
        while runner < len(s):
            if s[runner] in tempSet:
                if maxValue < runner - walker:
                    maxValue = runner - walker;

                while s[walker] != s[runner]:
                    tempSet.remove(s[walker])
                    walker += 1

                walker += 1
            else:
                tempSet.add(s[runner])

            runner += 1

        maxValue = max(maxValue, runner - walker)

        return maxValue

    def lengthOfLongestSubstring2(self, s):
        m = [-1 for i in range(256)]
        result = 0
        left = -1
        for i in range(len(s)):
            left = max(left, m[ord(s[i])])
            m[ord(s[i])] = i
            result = max(result, i - left)

        return result

    def lengthOfLongestSubstring3(self, s):
        result = 0
        left = 0
        right = 0
        t = set()
        while right < len(s):
            if s[right] in t:
                t.remove(s[left])
                left += 1
            else:
                t.add(s[right])
                result = max(result, len(t))
                right += 1

        return result

    def lengthOfLongestSubstring4(self, s):
        m = [-1 for i in range(128)]
        result = 0
        start = 0
        for i in range(len(s)):
            start = max(start, m[ord(s[i])]+1)
            result = max(result, i-start+1)
            m[ord(s[i])] = i

        return result


def main():
    obj = LongestSubstringWithoutRepeatingCharacters()
    print(obj.lengthOfLongestSubstring2("abcabcbb"))
    print(obj.lengthOfLongestSubstring2("bbbbb"))
    print(obj.lengthOfLongestSubstring2("pwwkew"))
    print()

    print(obj.lengthOfLongestSubstring2("abcabcbb"))
    print(obj.lengthOfLongestSubstring2("bbbbb"))
    print(obj.lengthOfLongestSubstring2("pwwkew"))
    print()

    print(obj.lengthOfLongestSubstring3("abcabcbb"))
    print(obj.lengthOfLongestSubstring3("bbbbb"))
    print(obj.lengthOfLongestSubstring3("pwwkew"))
    print()

    print(obj.lengthOfLongestSubstring4("abcabcbb"))
    print(obj.lengthOfLongestSubstring4("bbbbb"))
    print(obj.lengthOfLongestSubstring4("pwwkew"))

if __name__ == "__main__":
    main()
