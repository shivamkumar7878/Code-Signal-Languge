def stringsRearrangement(inputArray):
    import itertools
    possible_permutations=itertools.permutations(inputArray)
    
    for perm in possible_permutations:
        allmatch=True
        for i in range(len(perm)-1):
            if not isDifferByOneChar(perm[i], perm[i+1]):
                allmatch=False
                break
        if allmatch:
            return True 
    return False

def isDifferByOneChar(str1,str2):
    count=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            count+=1
    return count==1
