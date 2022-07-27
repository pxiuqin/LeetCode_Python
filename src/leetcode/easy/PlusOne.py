"""
 * https://leetcode.com/problems/plus-one/
 * 66. 加一
 * 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
 * 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
 * 你可以假设除了整数 0 之外，这个整数不会以零开头。
 * <p>
 * 示例1：
 * 输入：digits = [1,2,3]
 * 输出：[1,2,4]
 * 解释：输入数组表示数字 123。
 * <p>
 * 示例2：
 * 输入：digits = [4,3,2,1]
 * 输出：[4,3,2,2]
 * 解释：输入数组表示数字 4321。
 * <p>
 * 示例 3：
 * 输入：digits = [0]
 * 输出：[1]
 * <p>
 * 提示：
 * 1 <= digits.length <= 100
 * 0 <= digits[i] <= 9
"""


class PlusOne:
    def plusOne(self, digits):
        carry = 1
        v = []

        while len(digits) > 0:
            x = digits[len(digits) - 1]
            digits = digits[0:len(digits) - 1]
            x = x + carry
            v.append(x % 10)
            carry = x // 10

        if carry > 0:
            v.append(carry)

        v.reverse()
        return v


def main():
    obj = PlusOne()
    print(obj.plusOne([1, 2, 3]))
    print(obj.plusOne([1, 2, 9]))
    print(obj.plusOne([9, 9, 9]))
    print(obj.plusOne([4, 3, 2, 1]))
    print(obj.plusOne([0]))


if __name__ == "__main__":
    main()
