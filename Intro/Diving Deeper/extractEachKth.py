def extractEachKth(inputArray, k):
    ia=[]
    for i in range(len(inputArray)):
        if (i+1)%k!=0:
            ia.append(inputArray[i])
    return ia
