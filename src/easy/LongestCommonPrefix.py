"""
 * https://leetcode.com/problems/longest-common-prefix/
 * 14.最长共同前缀
 * Write a function to find the longest common prefix string amongst an array of strings.
 *
 * If there is no common prefix, return an empty string "".
 *
 * Example 1:
 *
 * Input: ["flower","flow","flight"]
 * Output: "fl"
 * Example 2:
 *
 * Input: ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 * 这题有好几种解法，个人认为会1，2的解法就可以了，但这种多方法解题的思路可以好好学习一下。具体可参考：Longest Common Prefix
 *
 * 1. 一个一个字符串取比较word by word matching：
 * 先拿前2个，从第一位开始比较，直到发现有不同的字符，此时前面一样的字符串在去和后面的字符串比较，直到结束。可以用递归。
 * Time: O(n*m) (n是字符串个数，m是字符串最长长度)  Space: O(m)
 *
 * 2. 一个字符一个字符的比较character by character matching：
 * 所有的字符串同时比较第1个，第2个.......，发现有不同的出现，之前一样的就是找到的最长共同前缀。Time: O(n*m) (n是字符串个数，m是字符串最长长度) Space: O(m)
 *
 * 3. divide and conquer:
 * 把所有字符串分成两组，分别去比较，最后都剩一个的时候，两组在比较。Time： O(n*m), Space: O(n*logm)
 *
 * 4. 二分法Binary Search：
 * 先找到最短的字符串，然后把这个最短的字符串二分成前面和后面两部分，前面的和所有剩下字符串比较，如果一样在比较后面的，如果有不一样的，则后面的部分不用比较了，前面的部分在二分比较。Time： O(n*m*logm), Space: O(m)
 *
 * 5. 使用Trie:
 * 首先了解Trie数据结构，然后把所有的字符串都执行一遍插入到Trie，然后读取Trie中最后一个没有分支的node，此时之前这些字符就是答案。
 * Time： O(n*m + m), Space: O(26*m*n) ~ O(m*n)
"""


class LongestCommonPrefix:
    def longestCommonPrefix(self, strs):
        word = ""
        if len(strs) <= 0:
            return word

        for i in range(1, len(strs[0])):  # longest prefix must <= len(strs[0])
            w = strs[0][0:i]
            match = True

            for j in range(1, len(strs)):
                if i > len(strs[j]) or w != strs[j][0:i]:
                    match = False
                    break

            if match == False:
                return word

            word = w

        return word


def main():
    obj = LongestCommonPrefix()
    print(obj.longestCommonPrefix(["flower", "flow", "flight"]))
    print(obj.longestCommonPrefix(["dog", "racecar", "car"]))


if __name__ == '__main__':
    main()
