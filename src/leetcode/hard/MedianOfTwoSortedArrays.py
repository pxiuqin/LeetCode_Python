"""
 * https://oj.leetcode.com/problems/median-of-two-sorted-arrays/
 * 4. 寻找两个正序数组的中位数
 * 给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和nums2。
 * 请你找出并返回这两个正序数组的 中位数 。
 * 分析:
 * 1. 使用归并的方式，合并两个有序数组，得到一个大的有序数组。大的有序数组的中间位置的元素，即为中位数。
 * 2. 不需要合并两个有序数组，只要找到中位数的位置即可。由于两个数组的长度已知，因此中位数对应的两个数组的下标之和也是已知的。维护两个指针，初始时分别指向两个数组的下标0的位置，每次将指向较小值的指针后移一位（如果一个指针已经到达数组末尾，则只需要移动另一个数组的指针），直到到达中位数的位置
 * 说明:第一种思路的时间复杂度是 O(m+n)，空间复杂度是 O(m+n)。第二种思路虽然可以将空间复杂度降到 O(1)，但是时间复杂度仍是 O(m+n)。题目要求时间复杂度是 O(log(m+n)),如果对时间复杂度的要求有 log，通常都需要用到二分查找实现
 * <p>
 * 示例 1：
 * 输入：nums1 = [1,3], nums2 = [2]
 * 输出：2.00000
 * 解释：合并数组 = [1,2,3] ，中位数 2
 * <p>
 * 示例 2：
 * 输入：nums1 = [1,2], nums2 = [3,4]
 * 输出：2.50000
 * 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 * <p>
 * 示例 3：
 * 输入：nums1 = [0,0], nums2 = [0,0]
 * 输出：0.00000
 * <p>
 * 示例 4：
 * 输入：nums1 = [], nums2 = [1]
 * 输出：1.00000
 * <p>
 * 示例 5：
 * 输入：nums1 = [2], nums2 = []
 * 输出：2.00000
 *
 * <p>
 * 提示：
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -106 <= nums1[i], nums2[i] <= 106
 *
 * <p>
 * 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
 * 思路:可以转化成寻找两个有序数组中的第 k 小的数，其中 k 为 (m+n)/2 或 (m+n)/2+1
 * 1. 如果 A[k/2−1]<B[k/2−1]，则比A[k/2−1] 小的数最多只有A的前 k/2−1 个数和 B 的前 k/2−1 个数，即比 A[k/2−1] 小的数最多只有 k−2 个，因此 A[k/2−1] 不可能是第k个数，A[0] 到 A[k/2−1] 也都不可能是第k个数，可以全部排除
 * 2. 如果 A[k/2−1]>B[k/2−1]，则可以排除 B[0] 到 B[k/2−1]
 * 3. 如果 A[k/2−1]=B[k/2−1]，则可以归入第一种情况处理
 * Cite:doc/img/Median Of Two Sorted Arrays.png
 * <p>
 * 举例说明:
 * A: 1 3 4 9
 * B: 1 2 3 4 5 6 7 8 9
 * 1. 两个有序数组的长度分别是 4 和 9，长度之和是 13，中位数是两个有序数组中的第 7 个元素，因此需要找到第k=7 个元素。比较两个有序数组中下标为 k/2−1=2 的数，即 A[2] 和 B[2]，如下面所示：
 * A: 1 3 4 9
 *      ↑
 * B: 1 2 3 4 5 6 7 8 9
 *      ↑
 * 2. 由于 A[2]>B[2]，因此排除 B[0] 到 B[2]，即数组 B 的下标偏移（offset）变为 3，同时更新 k 的值：k=k−k/2=4。 下一步寻找，比较两个有序数组中下标为 k/2−1=1 的数，即 A[1] 和 B[4]，如下面所示，其中方括号部分表示已经被排除的数。
 * A: 1 3 4 9
 *    ↑
 * B: [1 2 3] 4 5 6 7 8 9
 *          ↑
 * 3. 由于 A[1]<B[4]，因此排除 A[0] 到 A[1]，即数组 A 的下标偏移变为 2，同时更新 k 的值：k=k−k/2=2。下一步寻找，比较两个有序数组中下标为 k/2−1=0 的数，即比较 A[2] 和 B[3]，如下面所示，其中方括号部分表示已经被排除的数。
 * A: [1 3] 4 9
 *       ↑
 * B: [1 2 3] 4 5 6 7 8 9
 *         ↑
 * 4. 由于 A[2]=B[3]，根据之前的规则，排除 A 中的元素，因此排除 A[2]，即数组 A 的下标偏移变为 3，同时更新 k 的值：k=k−k/2=1。 由于 k 的值变成 1，因此比较两个有序数组中的未排除下标范围内的第一个数，其中较小的数即为第 k 个数，由于 A[3]>B[3]，因此第 k 个数是 B[3]=4
 * A: [1 3 4] 9
 *         ↑
 * B: [1 2 3] 4 5 6 7 8 9
 *         ↑
"""

import sys


class MedianOfTwoSortedArrays:
    def getKthElement(self, nums1, nums2, k):
        """
        主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
        这里的 "/" 表示整除
        nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
        nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
        取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
        这样 pivot 本身最大也只能是第 k-1 小的元素
        如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
        如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
        由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数

        :param nums1:
        :param nums2:
        :param k:
        :return:
        """
        length1 = len(nums1)
        length2 = len(nums2)
        index1 = 0
        index2 = 0

        while True:
            # 边界情况
            if index1 == length1:
                return nums2[index2 + k - 1]
            if index2 == length2:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])

            # 正常情况
            half = k // 2;
            newIndex1 = min(index1 + half, length1) - 1;
            newIndex2 = min(index2 + half, length2) - 1;
            pivot1 = nums1[newIndex1]
            pivot2 = nums2[newIndex2]

            if pivot1 <= pivot2:
                k -= newIndex1 - index1 + 1
                index1 = newIndex1 + 1
            else:
                k -= newIndex2 - index2 + 1
                index2 = newIndex2 + 1

    def findMedianSortedArrays(self, nums1, nums2):
        length1 = len(nums1)
        length2 = len(nums2)
        totalLenght = length1 + length2;
        if totalLenght % 2 == 1:
            midIndex = totalLenght // 2
            median = self.getKthElement(nums1, nums2, midIndex + 1)
            return median
        else:
            midIndex1 = totalLenght // 2 - 1
            midIndex2 = totalLenght // 2
            median = (self.getKthElement(nums1, nums2, midIndex1 + 1) + self.getKthElement(nums1, nums2,
                                                                                           midIndex2 + 1)) / 2
            return median


    def findMedianSortedArrays2(self, nums1, nums2):
        """
        Cite:https://blog.csdn.net/en_joker/article/details/107179641
        划分数组:将一个集合划分为两个长度相等的子集，其中一个子集中的元素总是大于另一个子集中的元素
        :param nums1:
        :param nums2:
        :return:
        """
        m = len(nums1)
        n = len(nums2)
        left = 0
        right = m
        if m > n:
            return self.findMedianSortedArrays2(nums2, nums1)

        # median1：前一部分的最大值
        # median2：后一部分的最小值
        median1 = 0
        median2 = 0

        while left <= right:
            # 前一部分包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
            # 后一部分包含 nums1[i .. m-1] 和 nums2[j .. n-1]
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            nums_i_1 = (-sys.maxsize - 1) if i == 0 else nums1[i - 1]
            nums_i = sys.maxsize if i == m else nums1[i]
            nums_j_1 = (-sys.maxsize - 1) if j == 0 else nums2[j - 1]
            nums_j = sys.maxsize if j == n else nums2[j]

            if nums_i_1 <= nums_j:
                median1 = max(nums_i_1, nums_j_1)
                median2 = min(nums_i, nums_j)
                left = i + 1
            else:
                right = i - 1

        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1


def main():
    obj = MedianOfTwoSortedArrays()
    print(obj.findMedianSortedArrays([1, 2], [3, 4]))
    print(obj.findMedianSortedArrays2([1, 2], [3, 4]))


if __name__ == "__main__":
    main()
