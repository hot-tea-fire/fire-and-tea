"""
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001

组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

本题含有多组输入用例，每组用例需要你将一个ip地址转换为整数、将一个整数转换为ip地址。
"""


def solution():
    while True:
        try:
            ip_list = list(input().split('.'))
            long_list = int(input())
        except:
            break
        else:
            a = ''
            for item in ip_list:
                tmp = str(bin(int(item))[2:]).rjust(8, '0')
                a += tmp
            print(int(a, 2))
            tmp = bin(long_list)[2:].rjust(32, '0')
            ip_res = []
            for item in range(0,32, 8):
                single = int(tmp[item:item + 8],2)
                ip_res.append(str(single))
            print('.'.join(ip_res))


if __name__ == '__main__':
    solution()
