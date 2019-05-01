def digitsum(num):
    return sum( [ int(char) for char in str(num) ] )
def digitDegree(n):
    if n/10==0:
        return 0
    
    counter=0
    while int(n/10)!=0:
        n = digitsum(n)
        counter+=1
    return counter
