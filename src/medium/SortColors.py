"""
 * https://leetcode.com/problems/sort-colors/
 * <p>
 * Given an array with n objects colored red, white or blue, sort them so that objects of
 * the same color are adjacent, with the colors in the order red, white and blue.
 * <p>
 * Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
 * <p>
 * Note:
 * You are not suppose to use the library's sort function for this problem.
 * <p>
 * Follow up:
 * > A rather straight forward solution is a two-pass algorithm using counting sort.
 * > First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array
 * with total number of 0's, then 1's and followed by 2's.
 * > Could you come up with an one-pass algorithm using only constant space?
"""


class SortColors:
    def sortColors(self, a):
        n = len(a)
        zero = 0
        two = n - 1

        i = 0
        while i <= two:
            if a[i] == 0:
                temp = a[zero]
                a[zero] = a[i]
                a[i] = temp

                zero += 1

            if a[i] == 2:
                temp = a[two]
                a[two] = a[i]
                a[i] = temp

                two -= 1
                i -= 1

            i += 1

        return a

    def swap(self, source, a, b):
        temp = source[a]
        source[a] = source[b]
        source[b] = temp

    def sortColors2(self, colors):
        left = 0
        right = len(colors) - 1

        i = 0
        while i <= right:
            if colors[i] == 0:
                self.swap(colors, i, left)
                left += 1
                i += 1
            elif colors[i] == 1:
                i += 1
            else:
                self.swap(colors, i, right)
                right -= 1

        return colors


def main():
    obj = SortColors()
    print(obj.sortColors([2, 0, 2, 1, 1, 0]))
    print(obj.sortColors2([2, 0, 2, 1, 1, 0]))
    print(obj.sortColors2([1, 0, 2, 1, 2, 0]))


if __name__ == "__main__":
    main()
