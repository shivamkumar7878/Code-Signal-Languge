def prefSum(a):
    return functools.reduce(lambda mem, x: mem + [mem[-1]+x], a, [0])[1:]
