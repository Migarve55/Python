#-------------------------------------------------------------------------------
# Name:        VisaNumberTester
# Purpose:
#
# Author:      UO257431
#
# Created:     30/09/2016
# Copyright:   (c) UO257431 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def main():
    #This variable is used to end the loop if necessary
    LOOP = True
    attemps = 3
    #Main loop
    while(LOOP):
        sum = 0
        rawVisaNumber = raw_input("Please enter your 16 digits (begins with 4 always) number: ") #Input
        if rawVisaNumber == "0":
            print("Operation cancelled")
            break;
        visaNumber = str(rawVisaNumber[::-1]) #This inverts the order of the digits
        #Itinerates throught all the digits
        for i in range(len(visaNumber)):
            if (i % 2 == 0): #even position
                sum += int(visaNumber[i])
            else: #odd position
                if (int(visaNumber[i]) * 2 > 9): #Checks if the double has two digits
                    numStr = str(int(visaNumber[i]) * 2) #Converts the number into a string
                    sum += int(numStr[0]) + int(numStr[1]) #Then it adds the two digits
                else:
                    sum += int(visaNumber[i]) * 2
        print(sum)
        if (sum % 10 == 0): # is valid
            print("The number is valid")
        else: #Is not a valid number, it substract one attemp.
            attemps -= 1
            print(("The number is invalid. you have %i attemps.") % attemps)

        if (attemps < 1): #If you have 0 attemps
            print("You have no more attemps. Visa card blocked.")
            LOOP = False

if __name__ == '__main__':
    main()
