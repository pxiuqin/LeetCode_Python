"""
 * https://leetcode.com/problems/permutations-ii
 * 47. 全排列 II
 * 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
 * <p>
 * 示例 1：
 * 输入：nums = [1,1,2]
 * 输出：
 * [[1,1,2],
 * [1,2,1],
 * [2,1,1]]
 * <p>
 * 示例 2：
 * 输入：nums = [1,2,3]
 * 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 * <p>
 * 提示：
 * 1 <= nums.length <= 8
 * -10 <= nums[i] <= 10
"""


class PermutationsII:
    # To deal with the duplication number, we need do those modifications:
    #    1) sort the array [pos..n].
    #    2) skip the same number.
    def permute(self, num):
        result = []
        result.append(num)

        if len(num) < 2:
            return result

        pos = 0
        while pos < len(num) - 1:
            size = len(result)
            for i in range(size):
                # sort the array , so that the same number will be together
                new_result = sorted(result[i][pos:])
                new_result = result[i][0:pos] + new_result

                for j in range(pos + 1, len(new_result)):
                    v = [each for each in new_result]

                    # skip the same number
                    if j > 0 and v[j] == v[j - 1]:
                        continue

                    temp = v[j]
                    v[j] = v[pos]
                    v[pos] = temp

                    result.append(v)

            pos += 1

        return result


def main():
    obj = PermutationsII()
    print(obj.permute([1, 1]))
    print(obj.permute([1, 1, 2]))
    print(obj.permute([1, 2, 3]))


if __name__ == '__main__':
    main()
