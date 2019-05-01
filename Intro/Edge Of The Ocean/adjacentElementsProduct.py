def adjacentElementsProduct(inputArray):

    for i in range(0,len(inputArray)-1):
        inputArray[i] = inputArray[i]*inputArray[i+1]
        print(inputArray)
    return max(inputArray[0:len(inputArray)-1])
