"""
 * https://leetcode.com/problems/reverse-integer/
 * 7. 整数反转
 * 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
 * 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
 * 假设环境不允许存储 64 位整数（有符号或无符号）。
 * <p>
 * 示例 1：
 * 输入：x = 123
 * 输出：321
 * <p>
 * 示例 2：
 * 输入：x = -123
 * 输出：-321
 * <p>
 * 示例 3：
 * 输入：x = 120
 * 输出：21
 * <p>
 * 示例 4：
 * 输入：x = 0
 * 输出：0
 *  
 * 提示：
 * -231 <= x <= 231 - 1
"""
import sys


class ReverseInteger:
    def reverse(self, x):
        y = 0
        while x != 0:
            n = x % 10 if x >= 0 else -(abs(x) % 10)
            if y > sys.maxsize // 10 or y < (-sys.maxsize - 1) // 10:
                return 0

            y = y * 10 + n
            x = x // 10 if x >= 0 else -(abs(x) // 10)

        return y


def main():
    obj = ReverseInteger()
    print(obj.reverse(123))
    print(obj.reverse(-123))


if __name__ == "__main__":
    main()
