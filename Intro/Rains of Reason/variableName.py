def variableName(name):
    if name[0].isdigit():
        return False
    
    for i in name:
        if i.isalnum() or i=="_":
            continue
        else:
            return False
        
    return True
