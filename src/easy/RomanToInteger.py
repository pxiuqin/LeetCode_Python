"""
* https://leetcode.com/problems/roman-to-integer/
* 13. 罗马数字转化成整数
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X+ II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X(10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

有几条须注意掌握：
1、基本数字Ⅰ、X 、C 中的任何一个，自身连用构成数目，或者放在大数的右边连用构成数目，都不能超过三个；放在大数的左边只能用一个
2、不能把基本数字V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；放在大数的右边采用相加的方式构成数目，只能使用一个
3、V 和X 左边的小数字只能用Ⅰ
4、L 和C 左边的小数字只能用X
5、D 和M 左边的小数字只能用C
"""


class RomanToInteger:
    def romanCharToInt(self, ch):
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return dict.get(ch, 0)

    def romanToInt(self, s):
        if len(s) <= 0:
            return 0

        result = self.romanCharToInt(s[0])
        for i in range(1, len(s)):
            prev = self.romanCharToInt(s[i - 1])
            curr = self.romanCharToInt(s[i])

            if prev < curr:
                result = result - prev + (curr - prev)  # IV,IX and so on
            else:
                result += curr

        return result


def main():
    obj = RomanToInteger()
    print(obj.romanToInt("III"))
    print(obj.romanToInt("IV"))
    print(obj.romanToInt("IX"))
    print(obj.romanToInt("LVIII"))
    print(obj.romanToInt("MCMXCIV"))


if __name__ == "__main__":
    main()
