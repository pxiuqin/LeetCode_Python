"""
 * https://leetcode.com/problems/maximum-subarray/
 53. 最大子序和
 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
 输出：6
 解释：连续子数组 [4,-1,2,1] 的和最大，为 6

 * Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
 * Example 1:
 * Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
 * Output: 6
 * Explanation: [4,-1,2,1] has the largest sum = 6.
 * <p>
 * Example 2:
 * Input: nums = [1]
 * Output: 1
"""


class MaximumSubarray:
    def maxSubArray(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        maxs = nums[0]
        index = 0

        for num in nums:
            # not start negate number
            if index < 0:
                index = 0  # return to zero

            index += num
            maxs = max(maxs, index)

        return maxs


def main():
    obj = MaximumSubarray()
    print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(obj.maxSubArray([4, -1, 2, 1]))


if __name__ == '__main__':
    main()
