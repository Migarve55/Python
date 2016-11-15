#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UO257431
#
# Created:     28/10/2016
# Copyright:   (c) UO257431 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------



def getContent(filename):
    with open(filename, "r") as data_file: #Opens the file
        data =data_file.readlines() #Reads the lines and return as a list string
    return data

def getDialCode(value):
    dc = "" #Dial code variable
    index = value.find('+') #Finds were the d.c. starts, with a '+'
    for c in value[index+1::]: #Itinerates throw the new string to find numbers
        if  c.isdigit(): #Check if is a number
            dc += c #Register the digits into the number
        else:  #If not, the d.c. has ended
            break
    return '+' + dc

def getCountry(value):
    country = "" #Country variable
    index = value.find(":") #Finds were the country name starts , it is the first ':'
    for c in value[index+1::]: #Itinerates throw the new string to find numbers
        if  c.isalpha(): #Check if is a letter
            country += c
        else:  #If not, the country name has ended
            break
    return country

def getCountries(codemin, codemax, content):
    linesList = [] #list of lines
    for line in content: #for each line in lines
        dc = int(getDialCode(line)[1::]) #We skip the '+' to parse it into a int
        if dc > codemin and dc < codemax: #Check if its inside the range
            linesList.append(line) #Appends the line
    return linesList

def createFile(filename, dialmin, dialmax):
    new_file = open('result.dial_code', "w") #Creates the file
    for line in getCountries(dialmin, dialmax, getContent(filename)): #For each dial code
        new_file.write(line)

def main():
    #DEBUG
    #print(getDialCode(getContent('dialCodes.json')[0]))
    #print(getCountry(getContent('dialCodes.json')[0]))
    #print(getCountries(0, 100, getContent('dialCodes.json')))
    #TestCreateFile
    createFile("dialCodes.json", 600, 700)

if __name__ == '__main__':
    main()
