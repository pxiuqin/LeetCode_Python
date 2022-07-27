"""
* https://leetcode.com/problems/reverse-nodes-in-k-group/
 * 25. K 个一组翻转链表
 * 给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
 * k是一个正整数，它的值小于或等于链表的长度。
 * 如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。
 * <p>
 * 进阶：
 * 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
 * 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
 *
 * 示例 1：
 * 输入：head = [1,2,3,4,5], k = 2
 * 输出：[2,1,4,3,5]
 * <p>
 * 示例 2：
 * 输入：head = [1,2,3,4,5], k = 3
 * 输出：[3,2,1,4,5]
 * <p>
 * 示例 3：
 * 输入：head = [1,2,3,4,5], k = 1
 * 输出：[1,2,3,4,5]
 * <p>
 * 示例 4：
 * 输入：head = [1], k = 1
 * 输出：[1]
 * <p>
 * 提示：
 * 列表中节点的数量在范围 sz 内
 * 1 <= sz <= 5000
 * 0 <= Node.val <= 1000
 * 1 <= k <= sz
"""

from src.easy.RemoveNthNodeFromEndOfList import *


class ReverseNodesInKGroup:
    def reverseList(self, head: LinkNode, k):
        pEnd = head
        while pEnd is not None and k > 0:
            pEnd = pEnd.next
            k -= 1

        # 如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序
        if k > 0:
            return head

        pHead = pEnd
        p = head
        while p is not pEnd:
            q = p.next
            p.next = pHead
            pHead = p
            p = q  # next

        return pHead

    def reverseKGroup(self, head: LinkNode, k):
        if k <= 0:
            return head
        fake = LinkNode(0)
        fake.next = head
        p = fake

        while p is not None:
            p.next = self.reverseList(p.next, k)
            for i in range(k):
                if p is not None:
                    p = p.next
        return fake.next


def main():
    obj = ReverseNodesInKGroup()
    head = LinkNode(1)
    head.list2link([2, 3, 4, 5])
    result = obj.reverseKGroup(head, 2)
    result.print()

    print()
    head = LinkNode(1)
    head.list2link([2, 3, 4, 5])
    result = obj.reverseKGroup(head, 3)
    result.print()

    print()
    head = LinkNode(1)
    head.list2link([2, 3, 4, 5])
    result = obj.reverseKGroup(head, 1)
    result.print()


if __name__ == '__main__':
    main()
