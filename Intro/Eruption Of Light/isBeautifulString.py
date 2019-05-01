from collections import Counter
import string

def isBeautifulString(inputString):
    c=Counter(inputString)
    ans=[]
    
    for k,v in sorted([(i,j) for i,j in c.items()]):
        ans.extend([all([x<=v for k1,x in c.items() if k1>k])])
        if k not in (set(string.ascii_lowercase[0:len(c.values())])):
            return False
    return all(ans)
    
            
