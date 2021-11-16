import itertools

"""
product('ABCD', repeat=2)       # 笛卡尔积
        AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations('ABCD', 2)         # 排列   有序
        AB AC AD BA BC BD CA CB CD DA DB DC
combinations('ABCD', 2)         # 组合   无序
        AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2)    
        AA AB AC AD BB BC BD CC CD DD
"""

"""
本题中，针对扑克牌 用 itertools.permutations(range(4),4)      # 不重复  共4个， 都参与
      针对运算符 用 itertools.product(map(str,range(4)), repeat=3))   # 可重复 共4个， 三个参与
"""


def tea():
    mapper = {'J': '11', 'Q': '12', 'K': '13', 'A': '1'}
    mapper_2 = {v: k for k, v in mapper.items()}
    input_str = ''.join(input().split(' '))
    if 'joker' in input_str.lower():
        print('ERROR')
        return
    li_number = [mapper.get(x, x) for x in input_str]
    for operate_one in itertools.product(('+', '-', '*', '/'), repeat=3):
        for number_one in itertools.permutations(li_number):
            res_ = '((' + number_one[0] + operate_one[0] + number_one[1] + ')' + operate_one[1] + number_one[2] + ')' + \
                   operate_one[2] + number_one[3]

            res = eval(res_)
            if res == 24 or res == 24.0:
                print(mapper_2.get(number_one[0], number_one[0]) + operate_one[0] + mapper_2.get(number_one[1],
                                                                                                 number_one[1]) +
                      operate_one[1] + mapper_2.get(number_one[2], number_one[2]) + operate_one[2] + mapper_2.get(
                    number_one[3], number_one[3]))
                return
    print('NONE')


if __name__ == '__main__':
    tea()
