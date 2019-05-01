def fibonacciList(n):
    return [[0] * x for x in functools.reduce(lambda y,_:y+[y[-2]+y[-1]] ,range(n-2),[0,1])]
