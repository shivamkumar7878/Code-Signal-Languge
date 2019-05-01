def calkinWilfSequence(number):
    def fractions():
        i=j=1
        while(True):
            yield[i,j]
            i,j=j,2*(i-i%j)+j-i
        

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
