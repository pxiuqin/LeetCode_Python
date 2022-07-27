"""
 * https://leetcode.com/problems/search-for-a-range/
 * 34. 查找范围
 *
 * Given a sorted array of integers, find the starting and ending position of a given target value.
 *
 * Your algorithm's runtime complexity must be in the order of O(log n).
 *
 * If the target is not found in the array, return [-1, -1].
 *
 * For example,
 * Given [5, 7, 7, 8, 8, 10] and target value 8,
 * return [3, 4].
 * <p>
 * 两次二分查找:
 * 如果我们不寻找那个元素先，而是直接相等的时候也向一个方向继续夹逼，如果向右夹逼，
 * 最后就会停在右边界，而向左夹逼则会停在左边界，如此用停下来的两个边界就可以知道结果了，只需要两次二分查找。
 * (这里有个小技巧，mid的取值，可以使得查找的方向向左或者向右偏移。)
"""


class SearchForARange:
    def searchRange(self, nums, target):
        result = [-1, -1]
        if nums is None:
            return result

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            # 向左夹逼则会停在左边界(= is key)
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            result[0] = start
        elif nums[end] == target:
            result[0] = end

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            # 如果向右夹逼最后就会停在右边界(= is key)
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            result[1] = end
        elif nums[start] == target:
            result[1] = start

        return result


def main():
    obj = SearchForARange()
    print(obj.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(obj.searchRange([5, 7, 8, 8, 8, 10], 8))
    print(obj.searchRange([5, 6, 7, 8, 9, 10], 8))


if __name__ == '__main__':
    main()
