"""
 https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 * 17. 电话号码的字母组合
 * 给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
 * 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
 * ./doc/img/0-100/17_telephone_keypad.png
 * <p>
 * 示例 1：
 * <p>
 * 输入：digits = "23"
 * 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
 * <p>
 * 示例 2：
 * 输入：digits = ""
 * 输出：[]
 * <p>
 * 示例 3：
 * 输入：digits = "2"
 * 输出：["a","b","c"]
 *
 * 提示：
 * 0 <= digits.length <= 4
 * digits[i] 是范围 ['2', '9'] 的一个数字。
 * <p>
 * <p>
 * Given a digit string, return all possible letter combinations that the number could represent.
 * <p>
 * A mapping of digit to letters (just like on the telephone buttons) is given below.
 * <p>
 * Input:Digit string "23"
 * Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 * <p>
 * Note:
 * Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class LetterCombinationsOfAPhoneNumber:
    @staticmethod
    def isNumber(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return True

    def letterCombinations(self, digits):
        phone = [[' ', '\0', '\0', '\0'],  # 0
                 ['\0', '\0', '\0', '\0'],  # 1
                 ['a', 'b', 'c', '\0'],  # 2
                 ['d', 'e', 'f', '\0'],  # 3
                 ['g', 'h', 'i', '\0'],  # 4
                 ['j', 'k', 'l', '\0'],  # 5
                 ['m', 'n', 'o', '\0'],  # 6
                 ['p', 'q', 'r', 's'],  # 7
                 ['t', 'u', 'v', '\0'],  # 8
                 ['w', 'x', 'y', 'z'],  # 9
                 ]
        result = []
        if len(digits) <= 0:
            return result

        for i in range(len(digits)):
            r = []
            if self.isNumber(digits[i]) == False:
                return r
            d = ord(digits[i]) - ord('0')
            if len(result) <= 0:
                for j in range(4):
                    s = phone[d][j]
                    if s != '\0':
                        result.append(s)
                continue

            for j in range(len(result)):
                for k in range(4):
                    s = phone[d][k]
                    if s != '\0':
                        r.append(result[j] + s)

            result = r

        return result


def main():
    obj = LetterCombinationsOfAPhoneNumber()
    print(obj.letterCombinations("23"))
    print(obj.letterCombinations(""))
    print(obj.letterCombinations("2"))


if __name__ == '__main__':
    main()
