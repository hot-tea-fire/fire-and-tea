ch = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']

while True:
    try:
        s = input()
        before, after = s.split('.')
        head, body, tail = '人民币', '', ''
        if after == '00':
            tail = '元整'
        else:
            if before == '0':
                tail = ''
            else:
                tail = '元'
            if after[0] != '0':
                tail += ch[int(after[0])] + '角'
            if after[1] != '0':
                tail += ch[int(after[1])] + '分'
        lst, i = [], len(before)
        while i - 4 >= 0:
            lst.insert(0, before[i-4:i])
            i -= 4
        if i > 0:
            lst.insert(0, before[:i])

        for i, num in enumerate(lst): # 如：['15', '1121']
            flag = True
            for j, c in enumerate(num):
                if c == '0':
                    if num == '0000':
                        if lst[-1] != '0000' and flag:
                            body += '零'
                            flag = False
                            continue
                    else:
                        if j != len(num)-1 and num[j+1] != '0' and flag:
                            body += '零'
                            flag = False
                            continue
                else:
                    if len(num[j:]) == 4:
                        body += ch[int(c)] + '仟'
                    elif len(num[j:]) == 3:
                        body += ch[int(c)] + '佰'
                    elif len(num[j:]) == 2:
                        if c != '1':
                            body += ch[int(c)] + '拾'
                        else:
                            body += '拾'
                    else:
                        body += ch[int(c)]
            if len(lst[i:]) == 3:
                body += '亿'
            elif len(lst[i:]) == 2 and num != '0000':
                body += '万'
        print(head + body + tail)

    except:
        break
