"""
* https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 * 19. 删除链表的倒数第 N 个结点
 * 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
 进阶：你能尝试使用一趟扫描实现吗？

 输入：head = [1,2,3,4,5], n = 2
 输出：[1,2,3,5]

 示例 2：
 输入：head = [1], n = 1
 输出：[]

 示例 3：
 输入：head = [1,2], n = 1
 输出：[1]

 提示：
 链表中结点的数目为 sz
 1 <= sz <= 30
 0 <= Node.val <= 100
 1 <= n <= sz
"""


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkList(object):
    def __init__(self):
        self._head = None

    def list2link(self, arr):
        self._head = None
        for each in arr:
            self.append(each)

    def isEmpyt(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next

        return count

    def items(self):
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next

    def append(self, item):
        node = Node(item)
        if self.isEmpyt():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        if index <= 0:
            self._head = Node(item)
        elif index > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self._head
        pre = None
        while cur is not None:
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next

    def remove4index(self, index):
        cur = self._head
        pre = None
        it = 0
        while cur is not None:
            if it == index:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                it += 1
                pre = cur
                cur = cur.next

    def print(self):
        cur = self._head
        while cur is not None:
            print(cur.item, end=',')
            cur = cur.next


class RemoveNthNodeFromEndOfList:
    def removeNthFromEnd(self, head: LinkList, n):
        head.remove4index(head.length() - n)
        return head


def main():
    obj = RemoveNthNodeFromEndOfList()
    head = LinkList()
    head.list2link([1, 2, 3, 4, 5])
    obj.removeNthFromEnd(head, 2)
    head.print()

    print()
    head.list2link([1])
    obj.removeNthFromEnd(head, 1)
    head.print()

    print()
    head.list2link([1, 2])
    obj.removeNthFromEnd(head, 1)
    head.print()


if __name__ == '__main__':
    main()
