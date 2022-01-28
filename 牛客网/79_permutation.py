"""
  /*
        给定参数n,从1到n会有n个整数:1,2,3,...,n,
        这n个数字共有n!种排列.
      按大小顺序升序列出所有排列的情况,并一一标记,
      当n=3时,所有排列如下:
      "123" "132" "213" "231" "312" "321"
      给定n和k,返回第k个排列.

      输入描述:
        输入两行，第一行为n，第二行为k，
        给定n的范围是[1,9],给定k的范围是[1,n!]。
      输出描述：
        输出排在第k位置的数字。

      实例1：
        输入:
          3
          3
        输出：
          231
        说明
          3的排列有123,132,213...,那么第三位置就是213

      实例2：
        输入
          2
          2
        输出：
          21
        说明
          2的排列有12,21，那么第二位置的为21
   */
"""

import itertools


def solution():
    while True:
        try:
            in_num = int(input())
            out_num = int(input())
        except:
            break
        else:
            list_in = [str(i) for i in range(1, in_num + 1)]
            out_list = list(itertools.permutations(list_in))
            li = []
            for item in out_list:
                li.append(''.join(item))
            li_2 = [int(x) for x in li]
            li_2.sort()
            print(li_2[out_num - 1])


if __name__ == '__main__':
    solution()
