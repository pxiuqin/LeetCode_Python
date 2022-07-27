"""
 * https://leetcode.com/problems/substring-with-concatenation-of-all-words/
 * 30. 串联所有单词的子串
 * <p>
 * 给定一个字符串s和一些 长度相同 的单词words 。找出 s 中恰好可以由words 中所有单词串联形成的子串的起始位置。
 * 注意子串要与words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑words中单词串联的顺序。
 * <p>
 * 示例 1：
 * 输入：s = "barfoothefoobarman", words = ["foo","bar"]
 * 输出：[0,9]
 * 解释：
 * 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
 * 输出的顺序不重要, [9,0] 也是有效答案。
 * <p>
 * 示例 2：
 * 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
 * 输出：[]
 * <p>
 * 示例 3：
 * 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
 * 输出：[6,9,12]
 *
 * 提示：
 * 1 <= s.length <= 10^4
 * s 由小写英文字母组成
 * 1 <= words.length <= 5000
 * 1 <= words[i].length <= 30
 * words[i]由小写英文字母组成
 *
 * 思路仍然是维护一个窗口，如果当前单词在字典中，则继续移动窗口右端，否则窗口左端可以跳到字符串下一个单词了
"""


class SubstringWithConcatenationOfAllWords:
    def findSubstring(self, S, L):
        result = []
        if len(S) <= 0 or len(L) <= 0:
            return result

        n = len(S)
        m = len(L)
        l = len(L[0])

        # put all of  words into a map
        expected = {}
        for i in range(m):
            if expected.__contains__(L[i]):
                expected[L[i]] = expected[L[i]] + 1
            else:
                expected[L[i]] = 1

        for i in range(l):
            actual = {}
            count = 0
            winLeft = i
            for j in range(i, n, l):
                word = S[j:j + l]

                # if not found ,then restart from j+1
                if expected.__contains__(word) is False:
                    actual.clear()
                    count = 0
                    winLeft = j + l
                    continue
                count += 1

                # count the number of "word"
                if actual.__contains__(word) is False:
                    actual[word] = 1
                else:
                    actual[word] = actual[word] + 1

                # If there is more appearance of "word" than expected
                if actual[word] > expected[word]:
                    tmp = ""
                    while tmp != word:
                        tmp = S[winLeft: winLeft + l]
                        count -= 1
                        actual[tmp] = actual[tmp] - 1
                        winLeft += l

                # if total count equals L's size, find one result
                if count == m:
                    result.append(winLeft)
                    tmp = S[winLeft:winLeft + l]
                    actual[tmp] = actual[tmp] - 1
                    winLeft += l
                    count -= 1

        return result


def main():
    obj = SubstringWithConcatenationOfAllWords()
    print(obj.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(obj.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
    print(obj.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))


if __name__ == '__main__':
    main()
