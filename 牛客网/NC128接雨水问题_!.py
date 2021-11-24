# by emz
# max water
# @param arr int整型一维数组 the array
# @return long长整型
#
class Solution:
    def maxWater(self , arr ):
        # write code here
        if arr == [] or len(arr) <= 2:
            return 0
        left,right = 0,len(arr) - 1
        sum1 = 0
        mark = min(arr[left], arr[right])
        while left < right:
            if arr[left] < arr[right]:
                left += 1
                if arr[left] < mark:
                    sum1 += mark - arr[left]
                else:
                    mark = min(arr[left], arr[right])
            else:
                right -= 1
                if arr[right] < mark:
                    sum1 += mark - arr[right]
                else:
                    mark = min(arr[left], arr[right])
        return sum1
