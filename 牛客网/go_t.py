if __name__ == '__main__':
    count = 0
    cost = 0
    for i in range(1, 1001111111):
        count += 1
        cost += 1
        if '4' in str(count):
            count = str(count).replace('4', '5')
        count = int(count)
        if count == 78597:
            print(cost)
            break
