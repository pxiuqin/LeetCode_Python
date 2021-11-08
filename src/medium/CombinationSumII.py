"""
 * https://leetcode.com/problems/combination-sum-ii/
 * 40. 组合总和 II
 * 给定一个数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
 * candidates中的每个数字在每个组合中只能使用一次。
 * 注意：解集不能包含重复的组合。

 * 示例1:
 * 输入: candidates =[10,1,2,7,6,1,5], target =8,
 * 输出:
 * [
 * [1,1,6],
 * [1,2,5],
 * [1,7],
 * [2,6]
 * ]
 *
 * 示例2:
 * 输入: candidates =[2,5,2,1,2], target =5,
 * 输出:
 * [
 * [1,2,2],
 * [5]
 * ]
 *
 * 提示:
 * 1 <=candidates.length <= 100
 * 1 <=candidates[i] <= 50
 * 1 <= target <= 30
"""


class CombinationSumII:
    def combinationSumHelper(self, candidates, start, target, solution: list, result):
        if target < 0:
            return

        if target == 0:
            result.append([i for i in solution])
            return

        for i in range(start, len(candidates)):
            # skip duplicates
            n = candidates[i]
            if i > start and n == candidates[i - 1]:
                continue

            solution.append(n)
            self.combinationSumHelper(candidates, i + 1, target - n, solution, result)  # i+1 can not be used multiple times
            solution.pop(len(solution) - 1)

    def combinationSum(self, candidates, target):
        result = []
        if len(candidates) <= 0:
            return result
        candidates = sorted(candidates)
        self.combinationSumHelper(candidates, 0, target, [], result)

        return result


def main():
    obj = CombinationSumII()
    print(obj.combinationSum([10, 1, 2, 7, 6, 1, 5], 8))
    print(obj.combinationSum([2, 5, 2, 1, 2], 5))


if __name__ == '__main__':
    main()
