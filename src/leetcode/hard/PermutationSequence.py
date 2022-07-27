"""
* https://leetcode.com/problems/permutation-sequence/
 * 60. 排列序列
 * 给出集合[1,2,3,...,n]，其所有元素共有n! 种排列。
 * <p>
 * 按大小顺序列出所有排列情况，并一一标记，当n = 3 时, 所有排列如下：
 * <p>
 * "123"
 * "132"
 * "213"
 * "231"
 * "312"
 * "321"
 * 给定n 和k，返回第k个排列。
 * <p>
 * 示例 1：
 * 输入：n = 3, k = 3
 * 输出："213"
 * <p>
 * 示例 2：
 * 输入：n = 4, k = 9
 * 输出："2314"
 * <p>
 * 示例 3：
 * 输入：n = 3, k = 1
 * 输出："123"
 * <p>
 * 提示：
 * 1 <= n <= 9
 * 1 <= k <= n!
 * <p>
 * method:
 * 1. 以某一数字开头的排列有(n-1)! 个。
 * 例如： 123， 132， 以1开头的是 2！个
 * 2. 所以第一位数字就可以用 （k-1） / (n-1)!  来确定 .这里K-1的原因是，序列号我们应从0开始计算，否则在边界时无法计算。
 * 3. 第二位数字。假设前面取余后为m，则第二位数字是 第 m/(n-2)! 个未使用的数字。
 * 4. 不断重复2，3，取余并且对(n-k)!进行除法，直至计算完毕
 * <p>
 * <p>
 * 回溯法:
 * 如何找出第16个（按字典序的）{1,2,3,4,5}的全排列？
 * 1. 首先用16-1得到15
 * 2. 用15去除4! 得到0余15
 * 3. 用15去除3! 得到2余3
 * 4. 用3去除2! 得到1余1
 * 5. 用1去除1! 得到1余0
 * 有0个数比它小的数是1，所以第一位是1
 * 有2个数比它小的数是3，但1已经在之前出现过了所以是4
 * 有1个数比它小的数是2，但1已经在之前出现过了所以是3
 * 有1个数比它小的数是2，但1,3,4都出现过了所以是5
 * 最后一个数只能是2
"""


class PermutationSequence:
    # Extreamly Optimized
    def getPermutation1(self, n, k):
        num = []
        total = 1
        for i in range(1, n + 1):
            num.append(i)
            total *= i  # total equal n!

        # invalid k
        if total < k:
            return []

        # Construct the k-th permutation with a list of n numbers
        # Idea: group all permutations according to their first number (so n groups, each of
        # (n-1)! numbers), find the group where the k-th permutation belongs, remove the common
        # first number from the list and append it to the resulting string, and iteratively
        # construct the (((k-1)%(n-1)!)+1)-th permutation with the remaining n-1 numbers
        group = total
        ss = []
        while n > 0:
            group = group // n
            idx = (k - 1) // group
            ss.append(num[idx])
            num.pop(idx)
            n -= 1

            # the next k also can be caculated like this
            # k=(k-1)%group+1
            k -= group * idx  # - outer size

        return ss

    ####################################################################################################################

    def factorial(self, n):
        total = 1
        for i in range(n, 0, -1):
            total *= i
        return total

    def getPermutation2(self, n, k):
        ls = []
        k = k - 1

        for i in range(n - 1, -1, -1):
            total = self.factorial(i)
            temp = k // total

            for j in range(1, n + 1):
                if ls.__contains__(j) is False:
                    temp -= 1
                    if temp < 0:
                        ls.append(j)
                        break

            k = k % total

        return ls

    ####################################################################################################################

    def nextPermutation(self, num: list):
        if len(num) <= 1:
            return num

        for i in range(len(num) - 1, 0, -1):
            if num[i - 1] < num[i]:
                j = len(num) - 1
                while num[i - 1] > num[j]:
                    j -= 1

                temp = num[i - 1]
                num[i - 1] = num[j]
                num[j] = temp

                num = num[:i] + list(reversed(num[i:]))
                return num

        num = reversed(num)
        return num

    # Optimization by determining the group
    def getPermutation3(self, n, k):
        num = []
        total = 1
        for i in range(1, n + 1):
            num.append(i)
            total *= i

        # invalid k
        if total < k:
            return []

        group = total // n
        idx = (k - 1) // group
        nn = num[idx]
        num.pop(idx)
        num.insert(0, nn)  # start permutation by group

        offset = (k - 1) % group  # offset is remain permutation
        for i in range(offset):
            num = self.nextPermutation(num)

        return num

    ####################################################################################################################

    # Time Limit Exceeded
    def getPermutation4(self, n, k):
        num = [i for i in range(1, n + 1)]

        for i in range(1, k):
            num = self.nextPermutation(num)

        return num


def main():
    obj = PermutationSequence()
    print(obj.getPermutation1(3, 1))
    print(obj.getPermutation1(3, 3))
    print(obj.getPermutation1(4, 9))

    print(obj.getPermutation2(3, 1))
    print(obj.getPermutation2(3, 3))
    print(obj.getPermutation2(4, 9))

    print(obj.getPermutation3(3, 1))
    print(obj.getPermutation3(3, 3))
    print(obj.getPermutation3(4, 9))

    print(obj.getPermutation4(3, 1))
    print(obj.getPermutation4(3, 3))
    print(obj.getPermutation4(4, 9))


if __name__ == "__main__":
    main()
