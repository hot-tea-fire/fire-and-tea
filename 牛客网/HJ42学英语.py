"""
1.在英语读法中三位数字看成一整体，后面再加一个计数单位。从最右边往左数，三位一单位，例如12,345 等
2.每三位数后记得带上计数单位 分别是thousand, million, billion.
3.公式：百万以下千以上的数 X thousand X, 10亿以下百万以上的数：X million X thousand X, 10 亿以上的数：X billion X million X thousand X. 每个X分别代表三位数或两位数或一位数。
4.在英式英语中百位数和十位数之间要加and，美式英语中则会省略，我们这个题目采用加上and，百分位为零的话，这道题目我们省略and
"""

num1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'seventeen', 'eighteen', 'nineteen']
num2 = [0, 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
        'seventy', 'eighty', 'ninety']


def eng_read(a):
    word = []
    if a >= 100:
        digit = a // 100
        word.append(num1[digit])
        word.append('hundred')
        if (a % 100) != 0:
            if (a % 100) < 20:
                word.append('and')
                word.append(num1[a % 100])
            else:
                num = (a % 100) // 10
                if num:
                    word.append('and')
                    word.append(num2[num])
                    ones_place = (a % 10)
                    if ones_place:
                        word.append(num1[ones_place])
                else:
                    word.append('and')
                    word.append(num1[a % 10])

    elif a < 20:
        word.append(num1[a])
    else:
        num = a // 10
        if num:
            word.append(num2[num])
            ones_place = (a % 10)
            if ones_place:
                word.append(num1[ones_place])
    return word


def solution():
    while True:
        try:
            number = int(input())
        except:
            break
        else:
            res_list = []
            bi = number // 1000000000
            mi = (number % 1000000000) // 1000000
            th = (number % 1000000) // 1000
            target = number % 1000
            if bi:
                res_list += num2[bi]
                res_list.append('billion')

            if mi:
                res_list += eng_read(mi)
                res_list.append('million')

            if th:
                res_list += eng_read(th)
                res_list.append('thousand')

            if target:
                res_list += eng_read(target)
            print(' '.join(res_list))


if __name__ == '__main__':
    solution()
