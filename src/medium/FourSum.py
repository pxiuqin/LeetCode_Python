"""
* https://leetcode.com/problems/4sum/
 * 18. 四数之和
 * 给定一个包含n 个整数的数组nums和一个目标值target，判断nums中是否存在四个元素 a，b，c和 d，使得a + b + c + d的值与target相等？找出所有满足条件且不重复的四元组。
 * 注意：答案中不可以包含重复的四元组。
 * <p>
 * <p>
 * 示例 1：
 * 输入：nums = [1,0,-1,0,-2,2], target = 0
 * 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
 * <p>
 * 示例 2：
 * 输入：nums = [], target = 0
 * 输出：[]
 *
 * 提示：
 * 0 <= nums.length <= 200
 * -10^9 <= nums[i] <= 10^9
 * -10^9 <= target <= 10^9
"""


class FourSum:
    def threeSum(self, num, target):
        result = []

        if len(num) < 3:
            return result

        # sort the array, this is the key
        num = sorted(num)
        n = len(num)
        for i in range(n - 2):
            # skip the duplication
            if i > 0 and num[i - 1] == num[i]:
                continue
            a = num[i]
            low = i + 1
            high = n - 1
            while low < high:
                b = num[low]
                c = num[high]
                if a + b + c == target:
                    # get the solution
                    v = []
                    v.append(a)
                    v.append(b)
                    v.append(c)
                    result.append(v)

                    # continue search for all triplet combinations summing to zero.
                    # skip the duplication
                    while low < n - 1 and num[low] == num[low + 1]:
                        low += 1
                    while high > 0 and num[high] == num[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif a + b + c > target:
                    # skip the duplication
                    while high > 0 and num[high] == num[high - 1]:
                        high -= 1
                    high -= 1
                else:
                    # skip the duplication
                    while low < n - 1 and num[low] == num[low + 1]:
                        low += 1
                    low += 1

        return result

    def fourSum(self, num, target):
        result = []
        if len(num) < 4:
            return result
        num = sorted(num)
        for i in range(len(num) - 3):
            # skip the duplication
            if i > 0 and num[i - 1] == num[i]:
                continue
            n = num[i + 1:len(num)]
            ret = self.threeSum(n, target - num[i])
            for each in ret:
                each.append(num[i])
                result.append(each)

        return result


def main():
    obj = FourSum()
    print(obj.fourSum([1, 0, -1, 0, -2, 2], 0))


if __name__ == '__main__':
    main()
