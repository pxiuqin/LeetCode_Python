"""
 * https://leetcode.com/problems/permutations/
 * 46. 全排列
 * 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
 * <p>
 * 示例 1：
 * 输入：nums = [1,2,3]
 * 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 * <p>
 * 示例 2：
 * 输入：nums = [0,1]
 * 输出：[[0,1],[1,0]]
 * <p>
 * 示例 3：
 * 输入：nums = [1]
 * 输出：[[1]]
 * <p>
 * 提示：
 * 1 <= nums.length <= 6
 * -10 <= nums[i] <= 10
 * nums 中的所有整数 互不相同
 * <p>
 * Given a collection of numbers, return all possible permutations.
 * <p>
 * For example,
 * [1,2,3] have the following permutations:
 * [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""


class Permutations:
    """
     *    The algorithm - Take each element in array to the first place.
     *
     *    For example:
     *
     *         0) initalization
     *
     *             pos = 0
     *             [1, 2, 3]
     *
     *         1) take each element into the first place,
     *
     *             pos = 1
     *             [1, 2, 3]  ==>  [2, 1, 3] , [3, 1, 2]
     *
     *             then we have total 3 answers
     *             [1, 2, 3],  [2, 1, 3] , [3, 1, 2]
     *
     *         2) take each element into the "first place" -- pos
     *
     *             pos = 2
     *             [1, 2, 3]  ==>  [1, 3, 2]
     *             [2, 1, 3]  ==>  [2, 3, 1]
     *             [3, 1, 2]  ==>  [3, 2, 1]
     *
     *             then we have total 6 answers
     *             [1, 2, 3],  [2, 1, 3] , [3, 1, 2], [1, 3, 2], [2, 3, 1], [3, 2, 1]
     *
     *          3) pos = 3 which greater than length of array, return.
     *
     """

    def permute(self, num):
        result = []
        result.append(num)

        if len(num) < 2:
            return result

        pos = 0  # the position of each traversal
        while pos < len(num) - 1:
            size = len(result)
            for i in range(size):
                # take each number to the first place (from pos to end)
                for j in range(pos + 1, len(result[i])):
                    v = [each for each in result[i]]  # new a list

                    # swap(j,pos) for v
                    t = v[j]
                    v[j] = v[pos]
                    v[pos] = t

                    result.append(v)

            pos += 1

        return result


def main():
    obj = Permutations()
    print(obj.permute([1, 2, 3]))
    print(obj.permute([0, 1]))
    print(obj.permute([1]))


if __name__ == '__main__':
    main()
