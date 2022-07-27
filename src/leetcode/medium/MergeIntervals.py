"""
 * https://leetcode.com/problems/merge-intervals/
 * 56. 合并区间
 * 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
 * <p>
 * 示例 1：
 * 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
 * 输出：[[1,6],[8,10],[15,18]]
 * 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
 * <p>
 * 示例2：
 * 输入：intervals = [[1,4],[4,5]]
 * 输出：[[1,5]]
 * 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
 * <p>
 * 提示：
 * 1 <= intervals.length <= 10^4
 * intervals[i].length == 2
 * 0 <= starti <= endi <= 10^4
 * <p>
 * Given a collection of intervals, merge all overlapping intervals.
 * <p>
 * For example,
 * Given [1,3],[2,6],[8,10],[15,18],
 * return [1,6],[8,10],[15,18].
"""

import functools


def cmp_f(x, y):
    if x[0] == y[0]:
        return x[1] - y[1]
    else:
        return x[0] - y[0]


class MergeIntervals:
    def merge(self, intervals: list):
        result = []
        if len(intervals) <= 0:
            return result

        # sort the inervals. Note:using the customized comparing function
        intervals = sorted(intervals, key=functools.cmp_to_key(cmp_f))

        for i in range(len(intervals)):
            size = len(result)

            # if the current intervals[i] is overlapped with previous interval.
            # merge them  together
            if size > 0 and result[size - 1][1] >= intervals[i][0]:
                result[size - 1][1] = max(result[size - 1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result


def main():
    obj = MergeIntervals()
    print(obj.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(obj.merge([[1, 4], [4, 5]]))


if __name__ == "__main__":
    main()
