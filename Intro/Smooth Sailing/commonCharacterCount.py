def commonCharacterCount(s1, s2):
    d1,d2={},{}
    for i in s1:
        #d.setdefault(i, []).append(s1.count(i))
        d1[i]=s1.count(i)
        
    for i in s2:
        d2[i]=s2.count(i)
    sum=0
    for k,v in sorted(d1.items()):
        if k in d2.keys():
            sum+=min(d2[k],d1[k])
    return sum
        
