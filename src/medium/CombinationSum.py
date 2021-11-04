"""
 * https://leetcode.com/problems/combination-sum/
 * 39. 组合总和
 * 给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
 * <p>
 * candidates中的数字可以无限制重复被选取。
 * <p>
 * 说明：
 * 所有数字（包括target）都是正整数。
 * 解集不能包含重复的组合。
 * <p>
 * 示例1：
 * 输入：candidates = [2,3,6,7], target = 7,
 * 所求解集为：
 * [
 * [7],
 * [2,2,3]
 * ]
 * <p>
 * 示例2：
 * 输入：candidates = [2,3,5], target = 8,
 * 所求解集为：
 * [
 * [2,2,2,2],
 * [2,3,3],
 * [3,5]
 * ]
 * <p>
 * 提示：
 * 1 <= candidates.length <= 30
 * 1 <= candidates[i] <= 200
 * candidate 中的每个元素都是独一无二的。
 * 1 <= target <= 500
"""


class CombinationSum:
    def combinationSumHelper(self, candidates, start, target, solution: list, result):
        if target < 0:
            return
        if target == 0:
            result.append([i for i in solution])
            return
        for i in range(start, len(candidates)):
            # skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            cand = candidates[i]
            solution.append(cand)
            self.combinationSumHelper(candidates, i, target - cand, solution, result)  # cand can be used multiple times
            solution.pop(len(solution) - 1)

    def combinationSum(self, candidates, target):
        result = []
        if len(candidates) <= 0:
            return result
        candidates = sorted(candidates)
        self.combinationSumHelper(candidates, 0, target, [], result)

        return result


def main():
    obj = CombinationSum()
    print(obj.combinationSum([2, 3, 6, 7], 7))
    print(obj.combinationSum([2, 3, 5], 8))


if __name__ == '__main__':
    main()
