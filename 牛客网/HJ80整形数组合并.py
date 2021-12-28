def solution(in_list: list, start: int, end: int):
    if start >= end:
        return
    i = start
    j = end
    mid = int(in_list[i])
    while i < j:
        while i < j and int(in_list[j]) >= mid:
            j -= 1
        in_list[i] = in_list[j]
        while i < j and int(in_list[j]) < mid:
            i += 1
        in_list[j] = in_list[i]
    in_list[i] = mid
    solution(in_list, start, i - 1)
    solution(in_list, j + 1, end)


if __name__ == '__main__':
    in_set = set()
    # while True:
    #     try:
    #         length = input()
    #         if not length:
    #             break
    #         in_list = input().split(' ')
    #         in_set.update(in_list)
    #     except:
    #         break
    in_set = list(in_set)
    # print(in_set)
    # print(type(in_set))
    in_set = ['1', '2', '5', '0', '-1', '3']
    solution(list(in_set), 0, len(in_set) - 1)
    print(in_set)
