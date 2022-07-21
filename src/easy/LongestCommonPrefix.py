"""
 * https://leetcode.com/problems/longest-common-prefix/
 * 14.最长共同前缀
 * Write a function to find the longest common prefix string amongst an array of
 * strings.
 * 
 * If there is no common prefix, return an empty string "".
 * 
 * Example 1:
 * Input: ["flower","flow","flight"]
 * Output: "fl"
 *
 * Example 2:
 * Input: ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 *
 * 这题有好几种解法，个人认为会1，2的解法就可以了，但这种多方法解题的思路可以好好学习一下。具体可参考：Longest Common Prefix
 * 
 * 1. 一个一个字符串取比较word by word matching（横向扫描）：
 * 先拿前2个，从第一位开始比较，直到发现有不同的字符，此时前面一样的字符串在去和后面的字符串比较，直到结束。可以用递归。
 * Time: O(n*m) (n是字符串个数，m是字符串最长长度) Space: O(m)
 * 解法参考图片：img\0-100\longest-common-prefix-1.png
 * 
 * 2. 一个字符一个字符的比较character by character matching（纵向扫描）：
 * 所有的字符串同时比较第1个，第2个.......，发现有不同的出现，之前一样的就是找到的最长共同前缀。Time: O(n*m)
 * (n是字符串个数，m是字符串最长长度) Space: O(m)
 * 解法参考图片：img\0-100\longest-common-prefix-2.png
 * 
 * 3. divide and conquer（分治法）:
 * 把所有字符串分成两组，分别去比较，最后都剩一个的时候，两组在比较。Time： O(n*m), Space: O(n*logm)
 * 解法参考图片：img\0-100\longest-common-prefix-3.png
 * 
 * 4. Binary Search（二分法）：
 * 先找到最短的字符串，然后把这个最短的字符串二分成前面和后面两部分，前面的和所有剩下字符串比较，如果一样在比较后面的，如果有不一样的，则后面的部分不用比较了，前面的部分在二分比较。Time：
 * O(n*m*logm), Space: O(m)
 * 解法参考图片：img\0-100\longest-common-prefix-4.png
 * 
 * 5. 使用Trie:
 * 首先了解Trie数据结构，然后把所有的字符串都执行一遍插入到Trie，然后读取Trie中最后一个没有分支的node，此时之前这些字符就是答案。
 * Time： O(n*m + m), Space: O(26*m*n) ~ O(m*n)
 *
 * 6. 先对所有子串排序再取首尾两个字串的前缀
"""


from turtle import st
from torch import le, sort


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

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]

    def longestCommonPrefix3(self, strs, start, end):
        # 如果无法再分的话就把单串返回
        if start == end:
            return strs[start]
        else:
            # 对数组中的每个串进行分治处理
            mid = (start+end)//2
            left = self.longestCommonPrefix3(strs, start, mid)
            right = self.longestCommonPrefix3(strs, mid+1, end)

            # 调用横向扫描方法
            return self.longestCommonPrefix([left, right])

    def longestCommonPrefix4(self, strs):
        if not strs:
            return ""

        # 找到最短的串长度，把这个长度作为可能最长的前缀
        min_length = min([len(e) for e in strs])
        start = 0
        end = min_length

        while start < end:
            # 把可能最长的一个公共前缀长度数，进行二分查找
            mid = (end-start+1)//2 + start
            new_strs = [e[0:mid] for e in strs]

            # 判断是否为子串
            is_cp = True if len(set(new_strs)) == 1 else False
            if is_cp:
                start = mid
            else:
                end = mid-1

        return strs[0][0:start]

    def longestCommonPrefix6(self, strs):
        if not strs:
            return ""

        # 对数组中串进行排序
        strs = sorted(strs)

        # 排序后只需获取第一个和最后一个串的最小长度
        min_length = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i < min_length and strs[0][i] == strs[-1][i]:
            i = i+1

        return strs[0][0:i]


def main():
    obj = LongestCommonPrefix()
    print(obj.longestCommonPrefix(["flower", "flow", "flight"]))
    print(obj.longestCommonPrefix(["dog", "racecar", "car"]))
    print()

    print(obj.longestCommonPrefix2(["flower", "flow", "flight"]))
    print(obj.longestCommonPrefix2(["dog", "racecar", "car"]))
    print()

    print(obj.longestCommonPrefix3(["flower", "flow", "flight"], 0, 2))
    print(obj.longestCommonPrefix3(["dog", "racecar", "car"], 0, 2))
    print()

    print(obj.longestCommonPrefix4(["flower", "flow", "flight"]))
    print(obj.longestCommonPrefix4(["dog", "racecar", "car"]))
    print()

    print(obj.longestCommonPrefix6(["flower", "flow", "flight"]))
    print(obj.longestCommonPrefix6(["dog", "racecar", "car"]))


if __name__ == '__main__':
    main()
