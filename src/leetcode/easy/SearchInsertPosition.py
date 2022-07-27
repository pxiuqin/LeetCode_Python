"""
 * https://oj.leetcode.com/problems/search-insert-position/
 * 35. 搜索插入位置
 * <p>
 * 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
 * 你可以假设数组中无重复元素。
 * <p>
 * 示例 1:
 * 输入: [1,3,5,6], 5
 * 输出: 2
 * <p>
 * 示例 2:
 * 输入: [1,3,5,6], 2
 * 输出: 1
 * <p>
 * 示例 3:
 * 输入: [1,3,5,6], 7
 * 输出: 4
 * <p>
 * 示例 4:
 * 输入: [1,3,5,6], 0
 * 输出: 0
"""


class SearchInsertPosition:
    def searchInsert(self, nums, target):
        if nums is None or len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if target <= nums[start]:
            return start
        if target <= nums[end]:
            return end

        return end + 1


def main():
    obj = SearchInsertPosition()
    print(obj.searchInsert([1, 3, 5, 6], 5))
    print(obj.searchInsert([1, 3, 5, 6], 2))
    print(obj.searchInsert([1, 3, 5, 6], 7))
    print(obj.searchInsert([1, 3, 5, 6], 0))


if __name__ == '__main__':
    main()
