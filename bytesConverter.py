
def convertBytesUnits(b):
    Sb = int(b / 1024)
    Ib = b % 1024
    n = 0
    index = [' ','K','M','G','T','Y']
    while(Sb > 1024):
        Sb = int(Ib / 1024)
        Ib = Ib % 1024
    if Sb > 0 and Ib > 0:
        return "Memory size: %i%cb, %i%cb" % (Sb,index[n+1],Ib,index[n])
    elif Sb > 0:
        return "Memory size: %i%cb" % (Sb,index[n+1])
    else:
        return "Memory size: %i%cb" % (Ib,index[n])
    

print(convertBytesUnits(1024898))

        
