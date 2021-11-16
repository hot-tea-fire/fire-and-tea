import itertools as it

while True:
    try:
        ls = input().split(" ")
        n = int(ls[0])
        s = []
        for i in range(n):
            s.append((tuple(ls[1 + i])))

        key = ls[n + 1]
        ind = int(ls[-1])
        bro = tuple(key)
        key = list(it.permutations(bro))

        end = []
        for i in range(n):
            if s[i] in key and s[i] != bro:
                end.append("".join(map(str, s[i])))

        bro_num = len(end)
        end.sort()

        print(bro_num)
        if ind <= bro_num:
            print(end[ind - 1])

    except:
        break
