"""
* https://leetcode.com/problems/first-missing-positive/
 * 41. 缺失的第一个正数
 * 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
 *
 * 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
 *
 * 示例 1：
 * 输入：nums = [1,2,0]
 * 输出：3
 *
 * 示例 2：
 * 输入：nums = [3,4,-1,1]
 * 输出：2
 *
 * 示例 3：
 * 输入：nums = [7,8,9,11,12]
 * 输出：1
 *
 * 提示：
 * 1 <= nums.length <= 5 * 10^5
 * -231 <= nums[i] <= 231 - 1
 *
 * <p>
 * Given an unsorted integer array, find the first missing positive integer.
 * <p>
 * For example,
 * Given [1,2,0] return 3,
 * and [3,4,-1,1] return 2.
 * <p>
 * Your algorithm should run in O(n) time and uses constant space.
"""

import sys


class FirstMissingPositive:
    """
     *  Idea:
     *
     *    We can move the num to the place which the index is the num.
     *
     *    for example,  (considering the array is zero-based.
     *       1 => A[0], 2 => A[1], 3=>A[2]
     *
     *    Then, we can go through the array check the i+1 == A[i], if not ,just return i+1;
     *
     *    This solution comes from StackOverflow.com
     *    http://stackoverflow.com/questions/1586858/find-the-smallest-integer-not-in-a-list
     """

    def firstMissingPositive_move(self, A):
        n = len(A)
        if n <= 0:
            return 1

        for i in range(n):
            num = A[i]
            while num > 0 and num < n and A[num - 1] != num:
                # swap(A[i],A[num-1])
                temp = A[i]
                A[i] = A[num - 1]
                A[num - 1] = temp

                num = A[i]

        for i in range(n):
            if i + 1 != A[i]:
                return i + 1

        return n + 1

    """
     *    The idea is simple:
     *
     *    1) put all of number into a map.
     *    2) for each number a[i] in array, remove its continous number in the map
     *        2.1)  remove ... a[i]-3, a[i]-2, a[i]-1, a[i]
     *        2.2)  remove a[i]+1, a[i]+2, a[i]+3,...
     *    3) during the removeing process, if some number cannot be found, which means it's missed.
     *
     *    considering a case [-2, -1, 4,5,6],
     *        [-2, -1] => missed 0
     *        [4,5,6]  => missed 3
     *
     *    However, we missed 1, so, we have to add dummy number 0 whatever.
     *
     *    NOTE: this solution is not constant space solution!!!!
     *
     """

    def firstMissingPositive_map(self, A):
        n = len(A)
        cache = {}
        for i in range(n):
            cache[A[i]] = i

        miss = sys.maxsize
        for i in range(n):
            if len(cache) <= 0:
                break

            x = A[i]
            if cache.__contains__(x) is False:
                continue

            # remove the ... x-3,x-2,x-1,x
            num = x
            while cache.__contains__(num):
                cache.pop(num)
                num -= 1

            if num > 0 and num < miss:
                miss = num

            # remove the x+1, x+2, x+3 ...
            num = x + 1
            while cache.__contains__(num):
                cache.pop(num)
                num += 1

            if num > 0 and num < miss:
                miss = num

        return miss


def main():
    obj = FirstMissingPositive()
    print(obj.firstMissingPositive_move([1, 2, 0]))
    print(obj.firstMissingPositive_move([3, 4, -1, 1]))
    print(obj.firstMissingPositive_move([7, 8, 9, 11, 12]))

    print(obj.firstMissingPositive_map([1, 2, 0]))
    print(obj.firstMissingPositive_map([3, 4, -1, 1]))
    print(obj.firstMissingPositive_map([7, 8, 9, 11, 12]))


if __name__ == '__main__':
    main()
