"""
* https://leetcode.com/problems/add-two-numbers/
 * 2. 两数相加
 * 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
 * 请你将两个数相加，并以相同形式返回一个表示和的链表。
 * 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
 * You are given two linked lists representing two non-negative numbers.
 * The digits are stored in reverse order and each of their nodes contain a single digit.
 * Add the two numbers and return it as a linked list.
 * <p>
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * <p>
 * 示例 1：
 * 输入：l1 = [2,4,3], l2 = [5,6,4]
 * 输出：[7,0,8]
 * 解释：342 + 465 = 807.
 * <p>
 * 示例 2：
 * <p>
 * 输入：l1 = [0], l2 = [0]
 * 输出：[0]
 * <p>
 * 示例 3：
 * 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 * 输出：[8,9,9,9,0,0,0,1]
 *  
 * 提示：
 * <p>
 * 每个链表中的节点数在范围 [1, 100] 内
 * 0 <= Node.val <= 9
 * 题目数据保证列表表示的数字不含前导零
 * <p>
"""


class AddTwoNumbers:
    def addTwoNumbers(self, l1: list, l2: list):
        result = []

        carry = 0
        len1 = len(l1)
        len2 = len(l2)
        size = len1 if len1 > len2 else len2
        for i in range(size):
            x = l1[i] if len1 > i else 0
            y = l2[i] if len2 > i else 0

            total = carry + x + y
            result.append(total % 10)
            carry = total // 10

        if carry > 0:
            result.append(carry % 10)

        return result


def main():
    obj = AddTwoNumbers()

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    print(obj.addTwoNumbers(l1, l2))


if __name__ == "__main__":
    main()
