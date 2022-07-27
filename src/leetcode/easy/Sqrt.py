"""
 * https://leetcode.com/problems/sqrtx/
 * 69. x 的平方根
 * 实现int sqrt(int x)函数。
 * 计算并返回x的平方根，其中x 是非负整数。
 * 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
 * <p>
 * 示例 1:
 * 输入: 4
 * 输出: 2
 * <p>
 * 示例 2:
 * 输入: 8
 * 输出: 2
 * 说明: 8 的平方根是 2.82842...,
 * 由于返回类型是整数，小数部分将被舍去。
 *
 * 牛顿法逼近解析： img(doc/img/0-100/Newton4Sqrt.png)
"""


class Sqrt:
    def sqrt1(self, x):
        if x <= 0:
            return 0

        # the sqrt is not greater than x/2+1
        e = x // 2 + 1
        s = 0

        # binary search
        while s <= e:
            mid = (s + e) // 2
            sq = mid * mid

            if sq == x:
                return mid

            if sq < x:
                s = mid + 1
            else:
                e = mid - 1

        return e

    # http://en.wikipedia.org/wiki/Newton%27s_method
    def sqrt2(self, x):
        if x == 0:
            return 0

        last = 0.0
        res = 1.0

        while res != last:
            last = res
            res = (res + x / res) / 2  # 牛顿法逼近

        return int(res)


def main():
    obj = Sqrt()
    print(obj.sqrt1(8))
    print(obj.sqrt1(4))
    print(obj.sqrt1(10))
    print(obj.sqrt1(80))

    print()
    print(obj.sqrt2(8))
    print(obj.sqrt2(4))
    print(obj.sqrt2(10))
    print(obj.sqrt2(80))


if __name__ == "__main__":
    main()
