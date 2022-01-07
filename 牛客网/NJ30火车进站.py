res = []


def dfs(wait, stack, out):
    if not wait and not stack:
        res.append(' '.join(map(str, out)))
    if wait:  # 入栈
        dfs(wait[1:], stack + [wait[0]], out)
    if stack:  # 出栈
        dfs(wait, stack[:-1], out + [stack[-1]])


while True:
    try:
        n, nums = int(input()), list(map(int, input().split()))
        dfs(nums, [], [])
        for i in sorted(res):
            print(i)
    except:
        break
