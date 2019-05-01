from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(map(lambda a: createNumber(a), filter(lambda a: int(createNumber(a)) % d == 0, product(digits, repeat = k))))
