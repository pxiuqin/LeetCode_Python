"""
* https://leetcode.com/problems/multiply-strings/
 * 43. 字符串相乘
 * 给定两个以字符串形式表示的非负整数num1和num2，返回num1和num2的乘积，它们的乘积也表示为字符串形式。
 *
 * 示例 1:
 *
 * 输入: num1 = "2", num2 = "3"
 * 输出: "6"
 * 示例2:
 *
 * 输入: num1 = "123", num2 = "456"
 * 输出: "56088"
 * 说明：
 *
 * num1和num2的长度小于110。
 * num1 和num2 只包含数字0-9。
 * num1 和num2均不以零开头，除非是数字 0 本身。
 * 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""


class MultiplyStrings:
    def multiply(self, num1, num2):
        n = len(num1)
        m = len(num2)
        res = [0 for i in range(m + n)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                res[i + j + 1] += int(num1[i]) * int(num2[j])

        carry = 0
        for i in range(len(res) - 1, -1, -1):
            res[i] += carry
            carry = res[i] // 10
            res[i] %= 10

        # 去掉最前的若干个0
        index = 0
        for i in range(len(res)):
            if res[i] != 0:
                index = i
                break

        multi = ""
        for j in range(index, len(res)):
            multi += str(res[j])

        return multi


def main():
    obj = MultiplyStrings()
    print(obj.multiply("2", "3"))
    print(obj.multiply("123", "456"))


if __name__ == '__main__':
    main()
