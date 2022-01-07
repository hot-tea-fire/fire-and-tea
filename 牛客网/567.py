num1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen']
num2 = [0, 0, 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
        'seventy', 'eighty', 'ninety']


# 100以内转英文
def n2w(n):
    if n > 0:
        if n < 20:
            word.append(num1[n])
        else:
            word.append(num2[n // 10])
            if n % 10 != 0:
                word.append(num1[n % 10])


# 1000以内转英文
def hun(n):
    if n >= 100:
        word.append(num1[n // 100])
        word.append('hundred')
        if n % 100 != 0:
            word.append('and')
    n2w(n % 100)


while True:
    try:
        n = int(input())
    except:
        break
    else:
        word = []
        a = n % 1000  # 个十百位
        b = (n // 1000) % 1000  # 个十百千
        c = (n // 1000000) % 1000  # 个十百m
        d = n // 1000000000  # 个十百b

        if d > 0:
            hun(d)
            word.append('billion')
        if c > 0:
            hun(c)
            word.append('million')
        if b > 0:
            hun(b)
            word.append('thousand')
        if a > 0:
            hun(a)
        print(' '.join(word))
