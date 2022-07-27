"""
 * https://leetcode.com/problems/jump-game/
 * 55. 跳跃游戏
 * 给定一个非负整数数组nums ，你最初位于数组的第一个下标 。
 * <p>
 * 数组中的每个元素代表你在该位置可以跳跃的最大长度。
 * <p>
 * 判断你是否能够到达最后一个下标。
 * <p>
 * 示例1：
 * 输入：nums = [2,3,1,1,4]
 * 输出：true
 * 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
 * <p>
 * 示例2：
 * 输入：nums = [3,2,1,0,4]
 * 输出：false
 * 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
 * <p>
 * 提示：
 * 1 <= nums.length <= 3 * 10^4
 * 0 <= nums[i] <= 10^5
"""


class JumpGame:
    def canJump(self, A: list):
        n = len(A)
        if n <= 0:
            return False

        # the basic idea is traverse array, maintain the most far can go
        coverPos = 0

        # the condition i<=coverPos means traverse all of covered position
        i = 0
        while i <= coverPos and i < n:
            if coverPos < A[i] + i:
                coverPos = A[i] + i

            if coverPos >= n - 1:
                return True

            i += 1

        return False


def main():
    obj = JumpGame()
    print(obj.canJump([2, 3, 1, 1, 4]))
    print(obj.canJump([3, 2, 1, 0, 4]))


if __name__ == "__main__":
    main()
