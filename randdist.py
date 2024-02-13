import random


def randomize(l: list) -> list:
    random.shuffle(l)
    
    return l


def distribute(l: list, div: int) -> list:
    ret = list()
    itv = len(l) / div
    for count in range(div):
        if count == div - 1:
            ret.append(l[round(itv * count): len(l)])
        else:
            ret.append(l[round(itv * count): round(itv * (count + 1))])

    return ret


def randis(l: list, div: int) -> list:
    l = randomize(l)
    l = distribute(l, div)

    return l
