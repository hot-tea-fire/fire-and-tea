"""
递归，又是看不太懂的一道题
"""

def dfs(five_list, three_list, other_list):
    if not other_list:
        if sum(five_list) == sum(three_list):
            return True
        else:
            return False
    if dfs(five_list + other_list[:1], three_list, other_list[1:]):
        return True
    if dfs(five_list, three_list+other_list[:1], other_list[1:]):
        return True


def solution():
    while True:
        try:
            n = int(input())
            m = list(map(int, input().split()))
        except:
            break
        else:
            five_list = []
            three_list = []
            other_list = []
            for item in m:
                if item % 5 == 0:
                    five_list.append(item)
                elif item % 3 == 0:
                    three_list.append(item)
                else:
                    other_list.append(item)
            if dfs(five_list, three_list, other_list):
                print('true')
            else:
                print('false')


if __name__ == '__main__':
    solution()
