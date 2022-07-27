"""
 * https://leetcode.com/problems/swap-nodes-in-pairs/
 * 24. 两两交换链表中的节点
 * 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
 * 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
 * <p>
 * 示例 1：
 * 输入：head = [1,2,3,4]
 * 输出：[2,1,4,3]
 * <p>
 * 示例 2：
 * 输入：head = []
 * 输出：[]
 * <p>
 * 示例 3：
 * 输入：head = [1]
 * 输出：[1]
 * <p>
 * 提示：
 * 链表中节点的数目在范围 [0, 100] 内
 * 0 <= Node.val <= 100
 * <p>
 * 进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。）
"""

from src.easy.RemoveNthNodeFromEndOfList import *


class SwapNodesInPairs:
    # just swap the node's value instead of node
    def swapPairs1(self, head: LinkNode):
        p = head
        while p is not None and p.next is not None:
            n = p.item
            p.item = p.next.item
            p.next.item = n
            p = p.next.next
        return head

    # swap the list nodes physically
    def swapPairs2(self, head: LinkNode):
        h = None

        # using 'p' to traverse the linked list
        p = head
        while p is not None and p.next is not None:
            # 'n' is 'p' `s next node and swap 'p' and 'n' physically
            n = p.next
            p.next = n.next
            n.next = p

            # using 'h' as 'p' `s previous node
            if h is not None:
                h.next = n
            h = p

            # determine the really 'head' pointer
            if head == p:
                head = n

            p = p.next

        return head

    def swapPairs3(self, head: LinkNode):
        # three pointers point current, previous and next node.
        curr = head
        pre = None
        nex = None
        while curr is not None and curr.next is not None:
            nex = curr.next

            # swap nodes
            curr.next = nex.next
            if pre is None:
                head = nex
                pre = nex
            else:
                pre.next = nex

            nex.next = curr

            # set the pointers to next place.
            pre = curr
            curr = curr.next

        return head


def main():
    obj = SwapNodesInPairs()
    head = LinkNode(1)
    head.list2link([2, 3, 4])
    result = obj.swapPairs1(head)
    result.print()

    print()
    head = LinkNode(1)
    head.list2link([2, 3, 4])
    result = obj.swapPairs2(head)
    result.print()

    print()
    head = LinkNode(1)
    head.list2link([2, 3, 4])
    result = obj.swapPairs3(head)
    result.print()


if __name__ == '__main__':
    main()
