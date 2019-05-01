def isLucky(n):
    sum1,sum2=0,0
    for i in range(0,str(n/(10**(len(str(n))/2))).find('.')):
        sum1 += int(str(n)[i])
    for i in range(str(n/(10**(len(str(n))/2))).find('.'),len(str(n))):
        sum2 += int(str(n)[i])
        
    if sum1==sum2:
        return True
    else:
        return False
