def findEmailDomain(address):
    try:
        local_part, _, address_part= address.split("@")    
    except:             
        local_part,  address_part= address.split("@")
        
    return address_part
