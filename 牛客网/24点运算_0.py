import time


def fun():
    while 1:
        try:
            entry = input().split(' ')
            t1 = time.time()
            number_mapper = {'J': 11, 'Q': 12, 'K': 13, 'A': 1}
            error_item = ['joker', 'JOKER']
            result = []
            for i in entry:
                if i in error_item:
                    print('ERROR')
                    return
                elif i in number_mapper:
                    result.append(number_mapper[i])
                else:
                    result.append(int(i))
            all_combination = []
            for i in result:
                middle_li = result[:]
                middle_li.remove(i)
                for j in middle_li:
                    middle_li_2 = middle_li[:]
                    middle_li_2.remove(j)
                    for k in middle_li_2:
                        middle_li_3 = middle_li_2[:]
                        middle_li_3.remove(k)
                        for m in middle_li_3:
                            all_combination.append([i, j, k, m])
            calculato = ['+', '-', '*', '/']
            calculato_conbination = []
            t0 = time.time()
            for i in calculato:
                for j in calculato:
                    for k in calculato:
                        calculato_conbination.append([i, j, k])
            result_mapper = {11: 'J', 12: 'Q', 13: 'K', 1: 'A'}
            for one in all_combination:
                for calcu in calculato_conbination:
                    t1 = calculate(one[0], one[1], calcu[0])
                    t2 = calculate(t1, one[2], calcu[1])
                    t3 = calculate(t2, one[3], calcu[2])
                    if t3 == 24:
                        for index, item in enumerate(one):
                            if item in result_mapper:
                                one[index] = result_mapper[item]

                        print(f'{one[0]}{calcu[0]}{one[1]}{calcu[1]}{one[2]}{calcu[2]}{one[3]}')
                        return

            print('NONE')
            return

        except Exception as e:
            print(f'{e}---')


def calculate(number1, number2, cal):
    if cal == '+':
        return number1 + number2
    elif cal == '-':
        return number1 - number2
    elif cal == '*':
        return number1 * number2
    elif cal == '/':
        return number1 / number2


if __name__ == '__main__':
    fun()
