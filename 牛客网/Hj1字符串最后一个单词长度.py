
def solution():
    while True:
        try:
            m = input().split()
        except:
            break
        else:
            print(len(m[-1]))



if __name__ == '__main__':
    solution()
