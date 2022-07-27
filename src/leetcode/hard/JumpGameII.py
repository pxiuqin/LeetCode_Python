"""
 * https://leetcode.com/problems/jump-game-ii/
 * 45. 跳跃游戏 II
 * 给你一个非负整数数组nums ，你最初位于数组的第一个位置。
 * 数组中的每个元素代表你在该位置可以跳跃的最大长度。
 * 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
 * 假设你总是可以到达数组的最后一个位置。
 * <p>
 * 示例 1:
 * 输入: nums = [2,3,1,1,4]
 * 输出: 2
 * 解释: 跳到最后一个位置的最小跳跃数是 2。
 * 从下标为 0 跳到下标为 1 的位置，跳1步，然后跳3步到达数组的最后一个位置。
 * <p>
 * 示例 2:
 * 输入: nums = [2,3,0,1,4]
 * 输出: 2
 * <p>
 * 提示:
 * 1 <= nums.length <= 10^4
 * 0 <= nums[i] <= 1000
"""


class JumpGameII:
    # Acutally, using the Greedy algorithm can have the answer
    def jump(self, A: list):
        n = len(A)
        if n <= 1:
            return 0

        steps = 0
        coverPos = 0

        i = 0
        while i <= coverPos and i < n:
            if A[i] == 0:
                return -1

            if coverPos < A[i] + i:
                coverPos = A[i] + i  # max cover
                steps += 1

            # if pos is end the return steps
            if coverPos >= n - 1:
                return steps

            # Greedy: find the next place which can have biggest distance
            nextPos = 0
            maxDistance = 0
            for j in range(i + 1, coverPos + 1):
                if A[j] + j > maxDistance:
                    maxDistance = A[j] + j  # find max distance for greedy
                    nextPos = j

            i = nextPos

        return steps


def main():
    obj = JumpGameII()
    print(obj.jump([2, 3, 1, 1, 4]))
    print(obj.jump([2, 3, 0, 1, 4]))


if __name__ == '__main__':
    main()
