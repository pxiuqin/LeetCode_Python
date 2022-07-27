
"""
快速排序
"""


from pyparsing import nums
from torch import le


class QuickSort:

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def partition(self, nums, left, right):
        v = nums[left]
        j = left

        for i in range(left+1, right):
            if nums[i] < v:
                j += 1
                if i == j:
                    continue
                self.swap(nums, i, j)

        self.swap(nums, left, j)
        return j

    def sort(self, nums, left, right):
        if left >= right:
            return

        p = self.partition(nums, left, right)
        self.sort(nums, left, p-1)
        self.sort(nums, p+1, right)

    def sort_start(self, nums):
        self.sort(nums, 0, len(nums)-1)


def main():
    obj = QuickSort()
    obj.sort_start([1, 0, 3, 2, 9, 6, 3, 6, 7, 2, 8, 3])
    print(nums)


if __name__ == "__main__":
    main()
