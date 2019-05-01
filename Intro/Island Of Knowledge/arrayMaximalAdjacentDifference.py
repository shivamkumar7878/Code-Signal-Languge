def arrayMaximalAdjacentDifference(inputArray):
    max_diff = {}
    for i in range(len(inputArray)):
        if i==0:
            max_diff.update({i:abs(inputArray[i+1]-inputArray[i])})
        elif i==len(inputArray)-1:
            max_diff.update({i:abs(inputArray[i]-inputArray[i-1])})
        else:
            max_diff.update({i:max(abs(inputArray[i+1]-inputArray[i]),
                                  abs(inputArray[i-1]-inputArray[i]))})
            
    max_=0
    for k,v in max_diff.items():
        if v > max_:
            max_=v
    return max_
