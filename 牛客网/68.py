"""
给定一个字符串S

        变化规则:
         交换字符串中任意两个不同位置的字符

        输入描述：
         一串小写字母组成的字符串
        输出描述：
         按照要求变换得到最小字符串

        实例1：
         输入：、
         abcdef
        输出
         abcdef

        实例2：
         输入
         bcdefa
         输出
         acdefb

        s都是小写字符组成
        1<=s.length<=1000

"""


def solution():
    while True:
        try:
            in_num = list(map(int, input().split(' ')))
        except:
            break
        else:
            sort_li = sorted(in_num, key=lambda x: abs(x))
            res = [sort_li[0], sort_li[1], abs(sort_li[0] + sort_li[1])]
            for item in range(2, len(in_num)):
                if abs(sort_li[item] + sort_li[item - 1]) < res[2]:
                    res = [sort_li[item], sort_li[item - 1], abs(sort_li[item] + sort_li[item - 1])]
            if sort_li[0] < sort_li[1]:
                print(str(res[0]) + " " + str(res[1]) + " " + str(res[2]))
            else:
                print(str(res[1]) + " " + str(res[0]) + " " + str(res[2]))


if __name__ == '__main__':
    solution()
