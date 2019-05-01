def allLongestStrings(inputArray):
    maxlength = 0
    outputArray=[]
    for i in range(0,len(inputArray)):
        maxlength = len(inputArray[i]) if len(inputArray[i]) > maxlength else maxlength
    for i in range(0,len(inputArray)):
        if len(inputArray[i])==maxlength:
            outputArray.append(inputArray[i])
    return outputArray
