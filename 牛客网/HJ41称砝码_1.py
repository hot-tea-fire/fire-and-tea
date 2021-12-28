"""
很好的一个方法

这个题我自己没有思路，看的别人的题解，感觉解释的特别清楚
https://github.com/ultraji/nowcoder
这个是她的git地址
利用集合去重的性质
先在集合里面添加0
当第一个砝码进来的时候
{0} 变成 {0,0+1}->{0,1}
当第二个砝码进来之后
{0，1} 变成 {0，1，0+1，1+1}--> {0,1,2}
当第三个砝码进来之后
{0,1,2} 变成{0，1，2，0+2，1+2，2+2}
---》 {0,1,2,3,4}
全部遍历一遍之后结束整个程序即可，这个就是所能得到的所有结果
"""

def solution():
    while True:
        try:
            n = int(input())
            m = list(map(int, input().split()))
            x = list(map(int, input().split()))
        except:
            break
        else:
            res_set = set([0])
            for index in range(n):
                for _ in range(x[index]):
                    for item in res_set.copy():
                        res_set.add(item + m[index])
            print(len(res_set))


if __name__ == '__main__':
    solution()
