"""
* https://leetcode.com/problems/insert-interval/
 * 57. 插入区间
 * 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
 * <p>
 * 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
 * <p>
 * 示例1：
 * 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
 * 输出：[[1,5],[6,9]]
 * <p>
 * 示例 2：
 * 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
 * 输出：[[1,2],[3,10],[12,16]]
 * 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10]重叠。
 * <p>
 * 示例 3：
 * 输入：intervals = [], newInterval = [5,7]
 * 输出：[[5,7]]
 * <p>
 * 示例 4：
 * 输入：intervals = [[1,5]], newInterval = [2,3]
 * 输出：[[1,5]]
 * <p>
 * 示例 5：
 * 输入：intervals = [[1,5]], newInterval = [2,7]
 * 输出：[[1,7]]
 * <p>
 * 提示：
 * 0 <= intervals.length <= 104
 * intervals[i].length == 2
 * 0 <=intervals[i][0] <=intervals[i][1] <= 105
 * intervals 根据 intervals[i][0] 按 升序 排列
 * newInterval.length == 2
 * 0 <=newInterval[0] <=newInterval[1] <= 105
"""

import functools
from src.medium.MergeIntervals import cmp_f


class InsertInterval:
    def merge(self, intervals: list):
        result = []
        if len(intervals) <= 0:
            return result

        # sort the intervals. Note:using the customized comparing function.
        intervals = sorted(intervals, key=functools.cmp_to_key(cmp_f))

        for i in range(len(intervals)):
            size = len(result)

            # if the current intervals[i] is overlapped with previous interval.
            # merge them together
            if size > 0 and result[size - 1][1] >= intervals[i][0]:
                result[size - 1][1] = max(result[size - 1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result


def main():
    obj = InsertInterval()
    print(obj.merge([[1, 3], [6, 9], [2, 5]]))
    print(obj.merge([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16], [4, 8]]))
    print(obj.merge([[1, 5], [2, 3]]))
    print(obj.merge([[1, 5], [2, 7]]))


if __name__ == "__main__":
    main()
