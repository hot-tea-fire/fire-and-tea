"""
梅花桩
"""


def solution():
    while True:
        try:
            numbers = int(input())
            num_list = list(map(int, input().split()))
        except:
            break
        else:
            max_res = 0
            for item in range(numbers):
                current_num = num_list[item]
                tmp_max_res = 1
                for next_num in num_list[item + 1:]:
                    if next_num > current_num:
                        current_num = next_num
                        tmp_max_res += 1
                max_res = max(max_res, tmp_max_res)
            print(max_res)


if __name__ == '__main__':

    solution()
