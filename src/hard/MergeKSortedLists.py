"""
* https://leetcode.com/problems/merge-k-sorted-lists/
 * 23. 合并K个升序链表
 * 给你一个链表数组，每个链表都已经按升序排列。
 * 请你将所有链表合并到一个升序链表中，返回合并后的链表。
 * <p>
 * 示例 1：
 * 输入：lists = [[1,4,5],[1,3,4],[2,6]]
 * 输出：[1,1,2,3,4,4,5,6]
 * 解释：链表数组如下：
 * [
 * 1->4->5,
 * 1->3->4,
 * 2->6
 * ]
 * 将它们合并到一个有序链表中得到。
 * 1->1->2->3->4->4->5->6
 * <p>
 * 示例 2：
 * 输入：lists = []
 * 输出：[]
 * <p>
 * 示例 3：
 * 输入：lists = [[]]
 * 输出：[]
 * <p>
 * 提示：
 * k == lists.length
 * 0 <= k <= 10^4
 * 0 <= lists[i].length <= 500
 * -10^4 <= lists[i][j] <= 10^4
 * lists[i] 按 升序 排列
 * lists[i].length 的总和不超过 10^4
 * <p>
 * 第一种方法:思路是先分成两个子任务，然后递归求子任务，最后回溯回来。先把k个list分成两半，然后继续划分，直到剩下两个list就合并起来
 * <p>
 * 第二种方法:这种方法用到了堆的数据结构，思路比较难想到，但是其实原理比较简单。
 * 维护一个大小为k的堆，每次取堆顶的最小元素放到结果中，然后读取该元素的下一个元素放入堆中，重新维护好。
 * 因为每个链表是有序的，每次又是去当前k个元素中最小的，所以当所有链表都读完时结束，这个时候所有元素按从小到大放在结果链表中。
 * 这个算法每个元素要读取一次，即是k*n次，然后每次读取元素要把新元素插入堆中要logk的复杂度，所以总时间复杂度是O(nklogk)。空间复杂度是堆的大小，即为O(k)

"""

from src.easy.RemoveNthNodeFromEndOfList import *


class MergeKSortedLists:
    def merge(self, l1, l2):
        dummy = LinkNode(0)
        dummy.next = l1
        cur = dummy
        while l1 is not None and l2 is not None:
            if l1.item < l2.item:
                l1 = l1.next
            else:
                nex = l2.next
                cur.next = l2
                l2.next = l1
                l2 = nex
            cur = cur.next
        if l2 is not None:
            cur.next = l2

        return dummy.next

    def helper(self, lists, l, r):
        if l < r:
            m = (l + r) // 2
            return self.merge(self.helper(lists, l, m), self.helper(lists, m + 1, r))
        return lists[l]

    def mergeKLists(self, lists):
        if lists is None or len(lists) == 0:
            return None
        return self.helper(lists, 0, len(lists) - 1)

def main():
    obj = MergeKSortedLists()
    # [[1,4,5],[1,3,4],[2,6]]
    node5 = LinkNode(5)
    node4 = LinkNode(4)
    node4.next = node5
    node1 = LinkNode(1)
    node1.next = node4

    node44 = LinkNode(4)
    node3 = LinkNode(3)
    node3.next = node44
    node11 = LinkNode(1)
    node11.next = node3

    node6 = LinkNode(6)
    node2 = LinkNode(2)
    node2.next = node6

    result = obj.mergeKLists([node1, node11, node2])
    result.print()


if __name__ == '__main__':
    main()
