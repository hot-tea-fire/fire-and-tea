import itertools


def search_bro_word():
    li = str(input()).split(' ')
    words = li[1:-2]
    target = li[-2]
    locate = li[-1]

    li_res = []
    all_situation = [''.join(x) for x in itertools.permutations(target, len(target))]
    for item in words:
        if item in all_situation and item != target:
            li_res.append(item)

    li_res.sort()
    print(len(li_res))
    if int(locate) < len(li_res):
        print(li_res[int(locate) - 1])


if __name__ == '__main__':
    search_bro_word()
