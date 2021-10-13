"""
* https://leetcode.com/problems/roman-to-integer/
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
