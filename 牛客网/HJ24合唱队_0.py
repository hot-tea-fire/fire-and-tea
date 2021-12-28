"""超时"""
def solution(len: int, hight_list: list):
    result_list = []
    for item in range(len):
        count_number = 0
        the_highest = hight_list[item]
        for i in hight_list[0:-item:-1]:
            if i > the_highest:
                count_number += 1
            else:
                the_highest = i
        the_highest = hight_list[item]
        for j in hight_list[item-1:]:
            if j < the_highest:
                count_number += 1
            else:
                the_highest = j
        result_list.append(count_number)
    print(max(result_list))


if __name__ == '__main__':
    len = int(input())
    hight_list = input().split(' ')
    solution(len, hight_list)
