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
import ctypes


class Pow:
    def recursion(self, x, n):
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
        if n == 1:
            return x

        # we`d better use unsigned right shift
        half = self.recursion(x, Pow.unsigned_right_shitf(n, 1))

        if n & 1 == 0:
            return half * half
        else:
            return half * half * x

    @staticmethod
    def int_overflow(val):
        maxint = 2147483647
        if not -maxint - 1 <= val <= maxint:
            val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
        return val

    @staticmethod
    def unsigned_right_shitf(n, i):
        if n < 0:
            n = ctypes.c_uint32(n).value

        if i < 0:
            return - Pow.int_overflow(n << abs(i))

        return Pow.int_overflow(n >> i)

    def pow1(self, x, n):
        if n == 0 or x == 1:
            return 1

        result = self.recursion(x, abs(n))

        if n > 0:
            return result
        else:
            return 1 / result

    def bitFunction(self, x, n):
        """
       * Solution with bit-manipulation
       * For example:
       * 9=1001
       * 3^9=(3^1)^1*(3^2)^0*(3^4)^0*(3^8)^1
       * Space is O(1), Time is O(logN)
        """
        multy = 1
        base = x
        i = n
        while i >= 1:
            if i & 1 > 0:
                multy *= base

            base *= base
            i = Pow.unsigned_right_shitf(i, 1)

        return multy

    def pow2(self, x, n):
        if n == 0 or x == 1:
            return 1

        # Avoid being out of bounds, we should cast into to long
        m = n
        result = self.bitFunction(x, abs(m))

        if n > 0:
            return result
        else:
            return 1 / result


def main():
    obj = Pow()
    print(obj.pow1(2, 10))
    print(obj.pow1(2.1, 3))
    print(obj.pow1(2, -2))

    print(obj.pow2(2, 10))
    print(obj.pow2(2.1, 3))
    print(obj.pow2(2, -2))


if __name__ == '__main__':
    # print(Pow.unsigned_right_shitf(-2,2))
    main()
