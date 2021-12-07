"""
* https://leetcode.com/problems/add-binary/
 * 67. 二进制求和
 * 给你两个二进制字符串，返回它们的和（用二进制表示）。
 * 输入为 非空 字符串且只包含数字1和0。
 * <p>
 * 示例1:
 * 输入: a = "11", b = "1"
 * 输出: "100"
 * <p>
 * 示例2:
 * 输入: a = "1010", b = "1011"
 * 输出: "10101"
 * <p>
 * 提示：
 * 每个字符串仅由字符 '0' 或 '1' 组成。
 * 1 <= a.length, b.length <= 10^4
 * 字符串如果不是 "0" ，就都不含前导零。
"""


class AddBinary:
    def addBinary(self, a, b):
        alen = len(a)
        blen = len(b)
        carry = False
        result = []

        while alen > 0 or blen > 0:
            abit = a[alen - 1] if alen > 0 else 0
            bbit = b[blen - 1] if blen > 0 else 0
            cbit = 1 if carry else 0

            result.append((abit + bbit + cbit) & 1)
            carry = (abit + bbit + cbit) > 1

            alen -= 1
            blen -= 1

        if carry is True:
            result.append(1)

        result.reverse()
        return result


def main():
    obj = AddBinary()
    print(obj.addBinary([1,1], [1]))
    print(obj.addBinary([1,0,1,0], [1,0,1,1]))


if __name__ == "__main__":
    main()
