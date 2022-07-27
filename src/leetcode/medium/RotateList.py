"""
 * https://leetcode.com/problems/rotate-list/
 * 61. 旋转链表
 * 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动k个位置。
 * 示例 1：
 * img(doc/img/0-100/rotate1.jpg)
 * 输入：head = [1,2,3,4,5], k = 2
 * 输出：[4,5,1,2,3]
 * <p>
 * 示例 2：
 * img(doc/img/rotate2.jpg)
 * 输入：head = [0,1,2], k = 4
 * 输出：[2,0,1]
 * <p>
 * 提示：
 * 链表中节点的数目在范围 [0, 500] 内
 * -100 <= Node.val <= 100
 * 0 <= k <= 2 * 10^9
"""

from src.easy.RemoveNthNodeFromEndOfList import LinkNode


class RotateList:
    def rotateRight(self, head: LinkNode, k):
        if head is None or k <= 0:
            return head

        # find the length of list
        size = 1
        p = head
        while p.next is not None:
            p = p.next
            size += 1

        # connect the tail to head
        p.next = head

        # find the left place (take care the case - k>size)
        k = size - k % size

        # find the place
        for i in range(k):
            p = p.next

        # break the list
        head = p.next
        p.next = None

        return head


def main():
    obj = RotateList()
    node = LinkNode(1)
    node.list2link([2, 3, 4, 5])
    node = obj.rotateRight(node, 2)
    node.print()


if __name__ == "__main__":
    main()
