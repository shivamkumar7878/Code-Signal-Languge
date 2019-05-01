def circleOfNumbers(n, firstNumber):
    first = [i for i in range(n) if i<n/2]
    second = [i for i in range(n) if i>=n/2]
    try:
        return second[first.index(firstNumber)]
    except:
        return first[second.index(firstNumber)]
