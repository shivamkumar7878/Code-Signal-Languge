def matrixElementsSum(matrix):
    d={}
    
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):  
            if matrix[i][j]==0:
                d.setdefault(i, []).append(j)

    rows = i

    for key,values in d.items():
        #print(key,values)  
        for i in range(0,len(matrix)):  
            if i>key:
                for val in values:
                    matrix[i][val]=0
                    #print(key,values,i)
    
    return sum(map(sum, matrix))
