"""
 * https://oj.leetcode.com/problems/string-to-integer-atoi/
 *
 * 8.Implement atoi to convert a string to an integer.
 *
 * Hint: Carefully consider all possible input cases. If you want a challenge,
 *       please do not see below and ask yourself what are the possible input cases.
 *
 * Notes:
 *   It is intended for this problem to be specified vaguely (ie, no given input specs).
 *   You are responsible to gather all the input requirements up front.
 *
 *
 * Requirements for atoi:
 *
 * The function first discards as many whitespace characters as necessary until the first
 * non-whitespace character is found. Then, starting from this character, takes an optional
 * initial plus or minus sign followed by as many numerical digits as possible, and interprets
 * them as a numerical value.
 *
 * The string can contain additional characters after those that form the integral number,
 * which are ignored and have no effect on the behavior of this function.
 *
 * If the first sequence of non-whitespace characters in str is not a valid integral number,
 * or if no such sequence exists because either str is empty or it contains only whitespace
 * characters, no conversion is performed.
 *
 * If no valid conversion could be performed, a zero value is returned. If the correct value
 * is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648)
 * is returned.
"""
import sys


class StringToIntegerAtoi:
    def atoi(self, source):
        result = 0
        source = source.strip()
        if source is None or source == "":
            return result

        neg = True if source[0] == '-' else False
        if neg or source[0] == '+':
            source = source[1:]

        for i in range(len(source)):
            digit = ord(source[i]) - ord('0')
            if digit > 9 or digit < 0:
                break

            if neg:
                if -result < (-sys.maxsize - 1 + digit) // 10:
                    return -sys.maxsize - 1
            else:
                if result > (sys.maxsize - digit) // 10:
                    return sys.maxsize

            result = result * 10 + digit

        return -result if neg else result


def main():
    obj = StringToIntegerAtoi()
    print(obj.atoi("123"))
    print(obj.atoi("   123"))
    print(obj.atoi("+123"))
    print(obj.atoi(" -123"))
    print(obj.atoi("123ABC"))
    print(obj.atoi("abc123ABC"))


if __name__ == "__main__":
    main()
