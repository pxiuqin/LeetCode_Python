"""
 * https://oj.leetcode.com/problems/3sum/
 * 15. 三数之和
 * 给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
 * 注意：答案中不可以包含重复的三元组。
 * <p>
 * 示例 1：
 * 输入：nums = [-1,0,1,2,-1,-4]
 * 输出：[[-1,-1,2],[-1,0,1]]
 * <p>
 * 示例 2：
 * 输入：nums = []
 * 输出：[]
 * <p>
 * 示例 3：
 * 输入：nums = [0]
 * 输出：[]
 *
 * 提示：
 * 0 <= nums.length <= 3000
 * -10^5 <= nums[i] <= 10^5
"""


class ThreeSum:
    """
     *   Similar like "Two Number" problem, we can have the simlar solution.
     *
     *   Suppose the input array is S[0..n-1], 3SUM can be solved in O(n^2) time on average by
     *   inserting each number S[i] into a hash table, and then for each index i and j,
     *   checking whether the hash table contains the integer - (s[i]+s[j])
     *
     *   Alternatively, the algorithm below first sorts the input array and then tests all
     *   possible pairs in a careful order that avoids the need to binary search for the pairs
     *   in the sorted list, achieving worst-case O(n^n)
     *
     *   Solution:  Quadratic algorithm
     *   http://en.wikipedia.org/wiki/3SUM
     *   排序预处理后，设置一个指针i 用来遍历，剩下两个元素，设置两个指针j 指向i+ 1, 和 k 指向 size() -1, 这两个指针从两侧向中间移动，寻找符合条件的元素。
     """

    def threeSum(self, num):
        result = []
        if len(num) < 3:
            return result

        # sort the array, this is the key
        num = sorted(num);

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
                if a + b + c == 0:
                    # got the solution
                    v = []
                    v.append(a)
                    v.append(b)
                    v.append(c)
                    result.append(v)

                    # continue search for all triplet combinations summing to zero, skip the duplication
                    while low < n - 1 and num[low] == num[low + 1]:
                        low += 1
                    while high > 0 and num[high] == num[high - 1]:
                        high -= 1

                    low += 1
                    high -= 1
                elif a + b + c > 0:
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

    @staticmethod
    def combination(v, k):
        result = []
        d = []
        n = len(v)
        for i in range(n):
            d.append(1 if i < k else 0)

        # 1) from the left, find the [1,0] pattern, change it to [0,1]
        # 2) move all of the 1 before the pattern to the most left side
        # 3) check all of 1 move to the right
        while True:
            tmp = []
            for x in range(n):
                if d[x] > 0:
                    tmp.append(v[x])

            tmp = sorted(tmp)
            result.append(tmp)

            # setp 1) find[1,0] pattern
            found = False
            ones = 0
            for i in range(n - 1):
                if d[i] == 1 and d[i + 1] == 0:
                    d[i] = 0
                    d[i + 1] = 1
                    found = True

                    # step 2) move all of right 1 to the most left side
                    for j in range(i):
                        d[j] = 1 if ones > 0 else 0
                        ones -= 1
                    break

                if d[i] == 1:
                    ones += 1
            if found == False:
                break

        return result

    def threeSum2(self, num):
        result = []
        r = self.combination(num, 3)
        for i in range(len(r)):
            if sum(r[i]) == 0 and not result.__contains__(r[i]):
                result.append(r[i])
        return result


def main():
    obj = ThreeSum()
    print(obj.threeSum([-1, 0, 1, 2, -1, -4]))
    print(obj.threeSum2([-1, 0, 1, 2, -1, -4]))


if __name__ == '__main__':
    main()
