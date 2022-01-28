"""
/*
        游戏规则：输入一个只包含英文字母的字符串，
        字符串中的俩个字母如果相邻且相同，就可以消除。
        在字符串上反复执行消除的动作，
        直到无法继续消除为止，
        此时游戏结束。
        输出最终得到的字符串长度。

        输出：原始字符串str只能包含大小写英文字母，字母的大小写敏感，长度不超过100，
        输出游戏结束后字符串的长度

        备注：输入中包含非大小写英文字母是均为异常输入，直接返回0。

        事例：mMbccbc输出为3
         */
"""
import re


def solution():
    while True:
        try:
            in_num = input()
        except:
            break
        else:
            if not in_num:
                break
            if re.findall(r'[^a-zA-Z]', in_num):
                print(0)
                continue
            in_num = list(in_num)
            subscript = 0
            while in_num[subscript] and subscript <= len(in_num) - 2:
                if in_num[subscript] == in_num[subscript + 1]:
                    del in_num[subscript + 1]
                    del in_num[subscript]
                    if subscript != 0:
                        subscript -= 1
                else:
                    subscript += 1
            print(len(in_num))


if __name__ == '__main__':
    solution()
    if re.findall(r'[^a-zA-Z]', 'asdfw3fagdagadadthas'):
        print(132)
