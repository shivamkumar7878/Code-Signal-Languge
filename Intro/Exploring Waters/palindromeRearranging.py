def palindromeRearranging(inputString):

    chars = [a for a in list(set(inputString))]
    occurences=[]
    for a in set(inputString):
        occurences.append(inputString.count(a))
    print(chars,occurences)
    odd_count=0
    
    for i in occurences:
        if i%2==1:
            odd_count+=1
                
    if odd_count == 1: return True
    if odd_count > 0 : return False
    
    return True
