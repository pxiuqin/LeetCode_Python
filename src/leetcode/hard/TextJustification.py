"""
 * https://leetcode.com/problems/text-justification/
 * 68. 文本左右对齐
 * 给定一个单词数组和一个长度maxWidth，重新排版单词，使其成为每行恰好有maxWidth个字符，且左右两端对齐的文本。
 * 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格' '填充，使得每行恰好有 maxWidth个字符。
 * 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
 * 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
 * <p>
 * 说明:
 * 单词是指由非空格字符组成的字符序列。
 * 每个单词的长度大于 0，小于等于maxWidth。
 * 输入单词数组 words至少包含一个单词。
 * <p>
 * 示例1:
 * 输入:
 * words = ["This", "is", "an", "example", "of", "text", "justification."]
 * maxWidth = 16
 * 输出:
 * [
 * "This  is  an",
 * "example of text",
 * "justification. "
 * ]
 * <p>
 * 示例2:
 * 输入:
 * words = ["What","must","be","acknowledgment","shall","be"]
 * maxWidth = 16
 * 输出:
 * [
 * "What  must  be",
 * "acknowledgment ",
 * "shall be    "
 * ]
 * 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
 * 因为最后一行应为左对齐，而不是左右两端对齐。
 * 第二行同样为左对齐，这是因为这行只包含一个单词。
 * <p>
 * 示例3:
 * 输入:
 * words = ["Science","is","what","we","understand","well","enough","to","explain",
 * "to","a","computer.","Art","is","everything","else","we","do"]
 * maxWidth = 20
 * 输出:
 * [
 * "Science is what we",
 * "understand   well",
 * "enough to explain to",
 * "a computer. Art is",
 * "everything else we",
 * "do         "
 * ]
"""

import math


class TextJustification:
    def fullJustify(self, words, L):
        result = []
        size = 0
        start = 0
        end = 0
        double_space = 0
        last_line = False

        for i in range(len(words)):
            size += len(words[i])
            if size + i - start > L or i == len(words) - 1:
                # remove the last one
                if size + i - start > L:
                    size -= len(words[i])
                    end = i - 1
                    last_line = False
                else:
                    end = i
                    last_line = True

                # calculate the space number
                space = L - size
                if last_line:
                    mspace = 1
                    extra = 0
                else:
                    mspace = math.floor(space / (end - start))
                    extra = space - mspace * (end - start)

                line = words[start]
                for j in range(start + 1, end + 1):
                    k = 0
                    while k < mspace and space > 0:
                        line += " "
                        k += 1
                        space -= 1
                    if j - start - 1 < extra:
                        line += " "
                        space -= 1
                    line += words[j]

                # add the rest space
                if space > 0:
                    for i in range(space, 0, -1):
                        line += " "

                result.append(line)
                start = i
                i = end
                size = 0

        return result


def main():
    obj = TextJustification()
    print(obj.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(obj.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))


if __name__ == "__main__":
    main()
