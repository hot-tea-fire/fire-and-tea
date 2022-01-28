"""
 所谓的水仙花数是指一个n位的正整数其各位数字的n次方的和等于该数本身，
    例如153=1^3+5^3+3^3,153是一个三位数
    输入描述
        第一行输入一个整数N，
        表示N位的正整数N在3-7之间包含3,7
        第二行输入一个正整数M，
        表示需要返回第M个水仙花数
    输出描述
        返回长度是N的第M个水仙花数，
        个数从0开始编号，
        若M大于水仙花数的个数返回最后一个水仙花数和M的乘积，
        若输入不合法返回-1

    示例一：

        输入
         3
         0
        输出
         153
        说明：153是第一个水仙花数
     示例二：
        输入
        9
        1
        输出
        -1
"""
from multiprocessing import Pool


def function(num, moudel_i, start):
    li = []
    for i in range(num, num + start):
        res = 0
        # print(i)
        for j in str(i):
            res += moudel_i[int(j)]
        if res == i:
            li.append(i)
            # print(i)
    return li


def solution():
    while True:
        in_num = input()
        if not in_num:
            break
        try:
            target = int(input())
            in_num = int(in_num)
        except ValueError:
            print(-1)
        else:
            if 3 <= in_num <= 7:
                start = 10 ** (in_num - 1)
                end = 10 ** in_num - 1
                moudel_i = {}
                for i in range(10):
                    moudel_i[i] = i ** in_num


                pool = Pool()
                li = []
                for i in range(start, end + 1, start):
                    l_res = pool.apply_async(func=function, args=(i, moudel_i, start))
                    li.append(l_res)
                res = []
                for item in li:
                    one_res = item.get()
                    if one_res:
                        res += one_res
                # print(res)
                # print(target)
                if len(res) >= target:
                    print(res[target])
                else:
                    print(-1)
            else:
                print(-1)


if __name__ == '__main__':
    solution()
