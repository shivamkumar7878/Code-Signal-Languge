def addBorder(picture):
    picture1=[]
    picture1.insert(0,'*'*(len(picture[0])+2))
    for pic in picture:
        picture1.append('*' + pic + '*') 
    picture1.append('*'*(len(picture[0])+2))
    return picture1
