
def isArmstrong(number, lenght):
    sumN = 0
    for i in range(lenght):
        sumN += (number%(10*10**i)-number%10**i)/(10**i)
    return sumN == number

print(isArmstrong(342,3))
    
