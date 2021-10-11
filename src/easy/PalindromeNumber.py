"""
* https://oj.leetcode.com/problems/palindrome-number/
 * 9. 回文数
 * 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
 * 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
 * <p>
 * 示例 1：
 * 输入：x = 121
 * 输出：true
 * <p>
 * 示例2：
 * 输入：x = -121
 * 输出：false
 * 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
 * <p>
 * 示例 3：
 * 输入：x = 10
 * 输出：false
 * 解释：从右向左读, 为 01 。因此它不是一个回文数。
 * <p>
 * 示例 4：
 * 输入：x = -101
 * 输出：false
 *
 * 提示：
 * -2^31<= x <= 2^31- 1
 *
 * 进阶：你能不将整数转为字符串来解决这个问题吗？
"""


class PalindromeNumber:
    def isPalindrome(self, x):
        if x < 0:
            return False

        if x < 10:
            return True

        n = x
        reverseX = 0
        while n > 0:
            reverseX = 10 * reverseX + n % 10
            n //= 10

        if reverseX == x:
            return True
        else:
            return False

    def isPalindromeStr(self, s):
        if s is None or s == "":
            return False

        if len(s) == 1:
            return True

        for i in range(len(s) // 2):
            left = s[i]
            right = s[len(s) - 1 - i]
            if left != right:
                return False

        return True


def main():
    obj = PalindromeNumber()
    print(obj.isPalindrome(121))
    print(obj.isPalindrome(-121))
    print(obj.isPalindrome(23))

    print(obj.isPalindromeStr("121"))
    print(obj.isPalindromeStr("-121"))
    print(obj.isPalindromeStr("23"))


if __name__ == "__main__":
    main()
