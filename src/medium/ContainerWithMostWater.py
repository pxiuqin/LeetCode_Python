"""
 * https://leetcode.com/problems/container-with-most-water/
 * 11. 盛最多水的容器
 * 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0) 。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
 * 说明：你不能倾斜容器。
 *
 * 示例 1：
 * 输入：[1,8,6,2,5,4,8,3,7]
 * 输出：49
 * 解释：图中(doc/img/ContainerWithMostWater.jpg)垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。
 * <p>
 * 示例 2：
 * 输入：height = [1,1]
 * 输出：1
 * <p>
 * 示例 3：
 * 输入：height = [4,3,2,1,4]
 * 输出：16
 * <p>
 * 示例 4：
 * 输入：height = [1,2,1]
 * 输出：2
 * <p>
 * 提示：
 * n = height.length
 * 2 <= n <= 3 * 10^4
 * 0 <= height[i] <= 3 * 10^4
"""
import sys


class ContainerWithMostWater:
    def maxArea(self, height):
        start = 0
        end = len(height) - 1
        multiplier = len(height) - 1
        maxarea = -sys.maxsize

        while multiplier != 0:
            maxarea = max(maxarea, min(height[start], height[end]) * multiplier)
            multiplier -= 1
            if height[start] > height[end]:  # find max
                end -= 1
            else:
                start += 1

        return maxarea


def main():
    obj = ContainerWithMostWater()
    print(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(obj.maxArea([1, 1]))
    print(obj.maxArea([4, 3, 2, 1, 4]))
    print(obj.maxArea([1, 2, 1]))


if __name__ == "__main__":
    main()
