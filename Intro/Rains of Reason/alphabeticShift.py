def alphabeticShift(inputString):
    return ''.join([chr(ord(i)+1)  if ord(i)<122 else 'a' for i in inputString]  )
    
