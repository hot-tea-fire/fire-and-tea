def fun(a, b):
    if a == 1:  # 当传入的值分子为1时，记录分母b
        l1.append(b)
    elif b % a == 0:  # 当a能被b整除时,记录分母b//a
        l1.append(b // a)
    elif b % (a - 1) == 0:  # 当a-1能被b整除时,记录分母b//(a-1) 和 b
        l1.append(b)
        l1.append(b // (a - 1))
    else:  # 利用公式算出最大子埃及分数、剩余分子、剩余分母。记录埃及分母c, z、m带入函数重新计算
        c = b // a + 1
        m = c * b
        z = a * c - b
        fun(z, m)
        l1.append(c)


if __name__ == '__main__':

    while True:
        try:
            l1, l2 = [], []  # l1用来存放找到的分母，来用来辅助计算
            a, b = map(int, input().split('/'))
            fun(a, b)
            l1.sort()
            for i in l1:
                l2.append('1/' + str(i))
            print('+'.join(l2))
        except:
            break
