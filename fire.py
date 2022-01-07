def bubb_sort(a_list):
    """冒泡排序"""
    for i in range(len(a_list) - 1):
        for j in range(len(a_list) - i - 1):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    print(a_list)


def select_sort(a_list):
    """选择排序"""

    for index, item in enumerate(a_list):
        standard = -1
        for last_index, last in enumerate(a_list[index + 1:]):
            if last < item:
                standard = last_index
        if standard != -1:
            a_list[index], a_list[standard] = a_list[standard], a_list[index]
    print(a_list)


def insert_sort(a_list):
    """插入排序"""
    res_list = []
    res_list.append(a_list[0])
    for item in a_list[1:]:
        for index, data in enumerate(res_list):
            if item >= data:
                continue
            else:
                res_list.insert(index, item)
                break
        else:
            res_list.append(item)
    print(res_list)


def shell_sort(a_list):
    """希尔排序，设置步长"""
    increment = len(a_list) / 3 + 1
    while increment > 0:
        break


if __name__ == '__main__':
    a_list = [10, 1, 5, 55, 38, 37, 37, 8, 3, 7, 9]
    bubb_sort(a_list)
    select_sort(a_list)
    insert_sort(a_list)
    shell_sort(a_list)
