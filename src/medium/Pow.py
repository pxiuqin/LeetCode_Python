"""
 * https://leetcode.com/problems/powx-n/
 * 50. Pow(x, n)
 * 实现pow(x, n)，即计算 x 的 n 次幂函数（即，x^n）。
 * <p>
 * 示例 1：
 * 输入：x = 2.00000, n = 10
 * 输出：1024.00000
 * <p>
 * 示例 2：
 * 输入：x = 2.10000, n = 3
 * 输出：9.26100
 * <p>
 * 示例 3：
 * 输入：x = 2.00000, n = -2
 * 输出：0.25000
 * 解释：2^-2 = 1/2^2 = 1/4 = 0.25
 * <p>
 * 提示：
 * -100.0 <x< 100.0
 * -2^31<= n <=2^31-1
 * -10^4 <= x^n <= 10^4
 */
"""


class Pow:
    """
    * Divide-and-Conquer method
    * For example:
    * <p>
    * 3^9=(3^4)^2*3
    * ↓
    * 3^4=(3^2)^2
    * ↓
    * 3^2=3*3
    * ↓
    * 3=3
    * <p>
    * So, both Space and Time are O(logN)
    """

    def recursion(self, x, n):
        if n == 1:
            return x

        # we`d better use unsigned right shift
        half = self.recursion(x, n > 1)

        if n & 1 == 0:
            return half * half
        else:
            return half * half * x


def main():
    obj = Pow()
    print(obj.recursion(2, 10))
    print(obj.recursion(2.1, 3))
    print(obj.recursion(2, -2))


if __name__ == '__main__':
    main()
