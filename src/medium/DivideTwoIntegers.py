"""
 * https://leetcode.com/problems/divide-two-integers/
 * 29.两数相除
 * Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
 * Return the quotient after dividing dividend by divisor.
 * The integer division should truncate toward zero.
 *
 * Example 1:
 * Input: dividend = 10, divisor = 3
 * Output: 3
 *
 * Example 2:
 * Input: dividend = 7, divisor = -3
 * Output: -2
 *
 * Note:
 * Both dividend and divisor will be 32-bit signed integers.
 * The divisor will never be 0.
 * Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
 *
 * 对于这道题，要求计算两个数字的商。
 * 在计算两个数字的商时，关键在于：
 * 使得被除数减去除数、且不让被除数变为0的次数。
 * <p>
 * 举个例子，假设被除数为15，除数为4，总的次数为m
 * 15 - 4 = 11 > 0，将除数扩大为原来的两倍，m = 1
 * 15 - 4*2 = 7 > 0，将除数扩大为原来的两倍， m = 2
 * 15 - 4*2^2 = -1 < 0，不可行，此时，我们得到新的被除数为：15 - 4*2 = 7，除数为4，因为被除数当前还大于除数，因此还需要继续进行；
 * 7 - 4 = 3 > 0，将除数扩大为原来的两倍，m = 3
 * 此时，被除数为7，除数为4*2 = 8，被除数小于除数，自然结束了。
 * 因为m = 3，我们有：15 = 3*4 + 3
 * 即，15/4 = 3
 * 同时，需要注意的是，当INT_MIN除以-1时，会造成溢出，因此，当被除数和除数分别是上述二者时，直接返回INT_MAX即可。
"""

import sys


class DivideTwoIntegers:
    def divide(self, dividend, divisor):
        sign = 1 if dividend / divisor > 0 else -1
        dvd = dividend if dividend > 0 else -dividend
        dvs = divisor if divisor > 0 else -divisor

        bit_num = [0 for i in range(33)]
        i = 0
        d = dvs
        bit_num[i] = d
        while d <= dvd:
            i += 1
            bit_num[i] = d = d << 1
        i -= 1

        result = 0
        while dvd >= dvs:
            if dvd >= bit_num[i]:
                dvd -= bit_num[i]
                result += (1 << i)
            else:
                i -= 1

        # becasue need to return `int`, so we need to check it is overflowed or not.
        if result > sys.maxsize and sign > 0:
            return sys.maxsize

        return result * sign

    def divide2(self, dividend, divisor):
        if dividend == sys.maxsize and divisor == -1:
            return sys.maxsize

        sign = 1 if dividend / divisor > 0 else -1
        dvd = abs(dividend)
        dvs = abs(divisor)
        res = 0

        # 当被除数大于等于除数时
        while dvd >= dvs:
            tmp = dvs
            m = 1
            while (tmp << 1) <= dvd:  # 当前够除
                tmp <<= 1  # 除数×2
                m <<= 1  # 除数构成个数×2

            dvd -= tmp  # 剩余的被除数
            res += m
        return sign * res


def main():
    obj = DivideTwoIntegers()
    print(obj.divide(10, 3))
    print(obj.divide2(10, 3))
    print(obj.divide(7, -3))
    print(obj.divide2(7, -3))


if __name__ == '__main__':
    main()
