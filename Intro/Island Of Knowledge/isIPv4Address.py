def isIPv4Address(inputString):
    ip_list=[]
    for i in inputString.split("."):
        try:
            ip_list.append(int(i))
        except:
            return False
    if len(ip_list)!=4:
        return False
    for i in ip_list:
        if int(i)>255 or int(i)<0:
            return False
    return True
        
