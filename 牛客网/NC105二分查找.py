"""
请实现有重复数字的升序数组的二分查找
给定一个 元素有序的（升序）长度为n的整型数组 nums 和一个目标值 target，
    写一个函数搜索 nums 中的第一个出现的target，如果目标值存在返回下标，否则返回 -1

输入      [1,2,4,4,5],4
返回值     2
说明      从左到右，查找到第1个为4的，下标为2，返回2

输入      [1,2,4,4,5],3
返回值     -1
"""

# 如果目标值存在返回下标，否则返回 -1
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        first_index = 0
        last_index = len(nums) - 1
        mid_index = len(nums) // 2
        while first_index <= last_index:
            if nums[mid_index] == target:
                while nums[mid_index] == target:
                    mid_index -= 1
                    if mid_index == -1:
                        return 0
                return mid_index + 1
            elif nums[mid_index] > target:
                last_index = mid_index - 1
                mid_index = (first_index + last_index) // 2
            elif nums[mid_index] < target:
                first_index = mid_index + 1
                mid_index = (first_index + last_index) // 2
        return -1


if __name__ == '__main__':
    slu = Solution()
    li = [-2, 1, 2]
    target = 4
    slu.search(li, target)

"""
    1.找第一个的时候要考虑到超出界限的时候
"""
