"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

输入      2
返回值     2
说明      青蛙要跳上两级台阶有两种跳法，分别是：先跳一级，再跳一级或者直接跳两级。因此答案为2
"""

# @param number int整型
# @return int整型
import time


class Solution:

    def __init__(self):
        self.remember_dict = {}
        self.dynamic_dict = {}

    # 递归
    def jumpFloor_recursion(self, number: int) -> int:
        if number == 0:
            return 1
        if number == 1:
            return 1
        return self.jumpFloor_recursion(number - 1) + self.jumpFloor_recursion(number - 2)

    # 记忆化搜索
    def jumpFloor_remember(self, number: int) -> int:
        if number == 0:
            return 1
        if number == 1:
            return 1
        if number in self.remember_dict:
            return self.remember_dict[number]
        else:
            record = self.jumpFloor_remember(number - 1) + self.jumpFloor_remember(number - 2)
            self.remember_dict[number] = record
            return record

    # 动态规划 从下往上计算
    def jumpFloor_dynamic(self, number: int) -> int:
        if number <= 1:
            return 1
        self.dynamic_dict[0] = 1
        self.dynamic_dict[1] = 1
        i = 2
        while i <= number:
            res = self.dynamic_dict[i - 1] + self.dynamic_dict[i - 2]
            self.dynamic_dict[i] = res
            i += 1
        return self.dynamic_dict[number]


if __name__ == '__main__':
    jf = Solution()
    t1 = time.time()
    a = jf.jumpFloor_recursion(40)
    t2 = time.time()
    b = jf.jumpFloor_remember(40)
    t3 = time.time()
    c = jf.jumpFloor_dynamic(40)
    t4 = time.time()

    print(f'jumpFloor_recursion  {a}  {t2 - t1} ')
    print(f'jumpFloor_remember  {b}  {t3 - t2} ')
    print(f'jumpFloor_dynamic  {c}  {t4 - t3} ')
