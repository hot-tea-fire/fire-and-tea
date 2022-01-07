
def solution():
    while True:
        try:
            m = input()
        except:
            break
        else:
            res = ''
            for item in m:
                if '0' <= item <= '8':
                    res += str(int(item) + 1)
                elif item == '9':
                    res += '0'
                elif 'a' <= item <= 'y':
                    res += chr(ord(item) - 31)
                elif item == 'z':
                    res += 'A'
                elif 'A' <= item <= 'Y':
                    res += chr(ord(item) + 33)
                elif item == 'Z':
                    res += 'a'
            print(res)
        try:
            m = input()
        except:
            break
        else:
            res = ''
            for item in m:
                if '1' <= item <= '9':
                    res += str(int(item) - 1)
                elif item == '0':
                    res += '9'
                elif 'b' <= item <= 'z':
                    res += chr(ord(item) - 33)
                elif item == 'a':
                    res += 'Z'
                elif 'B' <= item <= 'Z':
                    res += chr(ord(item) + 31)
                elif item == 'A':
                    res += 'z'
            print(res)



if __name__ == '__main__':
    solution()
