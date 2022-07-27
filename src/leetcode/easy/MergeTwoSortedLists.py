"""
 * https://leetcode.com/problems/merge-two-sorted-lists/
 * 21. 合并两个有序链表
 * 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
 * <p>
 * 示例 1：
 * 输入：l1 = [1,2,4], l2 = [1,3,4]
 * 输出：[1,1,2,3,4,4]
 * <p>
 * 示例 2：
 * 输入：l1 = [], l2 = []
 * 输出：[]
 * <p>
 * 示例 3：
 * 输入：l1 = [], l2 = [0]
 * 输出：[0]
 *
 * 提示：
 * 两个链表的节点数目范围是 [0, 50]
 * -100 <= Node.val <= 100
 * l1 和 l2 均按 非递减顺序 排列
"""

from src.easy.RemoveNthNodeFromEndOfList import LinkNode


class MergeTwoSortedLists:
    def mergeTwoLists(self, l1, l2):
        result = []
        l1 = sorted(l1)
        l2 = sorted(l2)
        count = len(l1) + len(l2)
        for i in range(count):
            if len(l1) > i and len(l2) > i and l1[i] < l2[i]:
                result.append(l1[i])
                l2.insert(i, 0)
            elif len(l2) > i:
                result.append(l2[i])
                if len(l1) > i:
                    l1.insert(i, 0)

        return result

    def mergeTwoLists2(self, l1: LinkNode, l2: LinkNode):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = LinkNode(0)
        out = head
        while l1 is not None and l2 is not None:
            if l1.item < l2.item:
                out.next = l1
                l1 = l1.next
            else:
                out.next = l2
                l2 = l2.next

            out = out.next

        if l1 is None and l2 is not None:
            out.next = l2
        elif l2 is None and l1 is not None:
            out.next = l1

        return head.next


def main():
    obj = MergeTwoSortedLists()
    print(obj.mergeTwoLists([1, 2, 4], [1, 3, 4]))
    print(obj.mergeTwoLists([1, 2], [3, 4]))

    node4 = LinkNode(4)
    node2 = LinkNode(2)
    node2.next = node4
    node1 = LinkNode(1)
    node1.next = node2

    node44 = LinkNode(4)
    node3 = LinkNode(3)
    node3.next = node44
    node11 = LinkNode(1)
    node11.next = node3
    result = obj.mergeTwoLists2(node1, node11)
    result.print()


if __name__ == '__main__':
    main()
