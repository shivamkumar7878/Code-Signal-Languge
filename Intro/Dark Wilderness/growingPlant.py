def growingPlant(upSpeed, downSpeed, desiredHeight):
    height=0
    counter=0
    while height<=desiredHeight:
        height+=upSpeed
        counter+=1
        if height>=desiredHeight:
            return counter
        else:
            height-=downSpeed            
        
    return counter
