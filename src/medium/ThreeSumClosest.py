"""
* https://leetcode.com/problems/3sum-closest/
 * 16. 最接近的三数之和
 * 给定一个包括n 个整数的数组nums和 一个目标值target。
 * 找出nums中的三个整数，使得它们的和与target最接近。返回这三个数的和。
 * 假定每组输入只存在唯一答案。
 * <p>
 * 示例：
 * 输入：nums = [-1,2,1,-4], target = 1
 * 输出：2
 * 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 *
 * 提示：
 * 3 <= nums.length <= 10^3
 * -10^3<= nums[i]<= 10^3
 * -10^4<= target<= 10^4
"""

import sys


class ThreeSumClosest:
    def threeSumClosest(self, num, target):
        # sort the array
        num = sorted(num)
        n = len(num)
        distance = sys.maxsize
        result = 0

        for i in range(n - 2):
            # skip the duplication
            if i > 0 and num[i - 1] == num[i]:
                continue

            a = num[i]
            low = i + 1
            high = n - 1

            # convert the 3sum to 2sum problem
            while low < high:
                b = num[low]
                c = num[high]
                total = a + b + c
                if total - target == 0:
                    # get the final solution
                    return target
                else:
                    # tracking the minmal distance
                    if abs(total - target) < distance:
                        distance = abs(total - target)
                        result = total

                    if total - target > 0:
                        # skip the dumplication
                        while high > 0 and num[high - 1] == num[high]:
                            high -= 1
                        # move the 'high' pointer
                        high -= 1
                    else:
                        # skip the duplication
                        while low < n and num[low + 1] == num[low]:
                            low += 1
                        # move the 'low' pointer
                        low += 1

        return result


def main():
    obj = ThreeSumClosest()
    print(obj.threeSumClosest([-1, 2, 1, -4], 1))
    print(obj.threeSumClosest([-4, -1, -1, 1, 2], 2))
    print(obj.threeSumClosest([-4, -1, -1, 1, 2], 5))


if __name__ == '__main__':
    main()
