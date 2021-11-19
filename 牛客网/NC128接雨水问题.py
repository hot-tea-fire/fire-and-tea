"""
给定一个整形数组arr，已知其中所有的值都是非负的，将这个数组看作一个柱子高度图，计算按此排列的柱子，下雨之后能接多少雨水。(数组以外的区域高度视为0)

数据范围：0≤n≤1000000，数组中每个值满足 0<val≤1000000000
要求：空间复杂度 O(1)O(1),时间复杂度 O(n)O(n)

输入：
[3,1,2,5,2,4]
返回值：
5
说明：
数组 [3,1,2,5,2,4] 表示柱子高度图，在这种情况下，可以接 5个单位的雨水，蓝色的为雨水 ，如题面图。
"""

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# max water
# @param arr int整型一维数组 the array
# @return long长整型
#
from typing import List


class Solution:
    def maxWater(self, arr: List[int]) -> int:
        # write code here
        left_altitude = 0
        left_index = None
        for index, item in enumerate(arr[::-1]):
            if item > left_altitude:
                left_altitude = item
                left_index = -index
        right_altitude = 0
        right_index = None
        for index, item in enumerate(arr):
            if item > right_altitude:
                right_altitude = item
                right_index = index
        all_water = 0
        li_pool = []
        first = arr[right_index]
        for item in arr[left_index + 1:right_index]:
            if item > first:
                for i in li_pool:
                    all_water = all_water + i

            else:
                li_pool.append(item)
        print(all_water)
        return all_water


if __name__ == '__main__':
    in_str = eval(input())

    s = Solution()
    s.maxWater(in_str)
