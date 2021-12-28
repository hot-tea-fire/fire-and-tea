def solution(in_list: list):
    direction = ['A', 'D', 'W', 'S']
    coordinate = [0, 0]
    for item in in_list:
        if not item or item[0] not in direction:
            continue
        flag = True
        for i in item[1:]:
            if str(0) <= str(i) <= str(9):
                continue
            else:
                flag = False
                break
        if flag:
            if item[0] == 'A':
                coordinate[0] -= int(item[1:])
            elif item[0] == 'D':
                coordinate[0] += int(item[1:])
            elif item[0] == "W":
                coordinate[1] += int(item[1:])
            elif item[0] == "S":
                coordinate[1] -= int(item[1:])
    print(str(coordinate[0]) + ',' + str(coordinate[1]))


if __name__ == '__main__':
    in_str = input().split(';')
    solution(in_str)
