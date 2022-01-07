"""
1.在英语读法中三位数字看成一整体，后面再加一个计数单位。从最右边往左数，三位一单位，例如12,345 等
2.每三位数后记得带上计数单位 分别是thousand, million, billion.
3.公式：百万以下千以上的数 X thousand X, 10亿以下百万以上的数：X million X thousand X, 10 亿以上的数：X billion X million X thousand X. 每个X分别代表三位数或两位数或一位数。
4.在英式英语中百位数和十位数之间要加and，美式英语中则会省略，我们这个题目采用加上and，百分位为零的话，这道题目我们省略and
"""

num1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'seventeen', 'eighteen', 'nineteen']
num2 = [0, 0, 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
        'seventy', 'eighty', 'ninety']

word = []

def eng_read(a):
    if a > 100:
        word


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
            pass


if __name__ == '__main__':
    solution()
