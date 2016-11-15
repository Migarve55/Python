import datetime

#Solution in one line, using a library
print(datetime.date.fromordinal(datetime.date(int(input("Year: ")), int(input("Month: ")), int(input("Day: "))).toordinal()+1))

#Solution in n lines, using normal python capabilities

#Total lines of code: 19

isLeapYear = lambda y: (y%4==0) and (y%100!=0 or (y%100==0 and y%400==0))
#Checks if the day entered is valid
def isDayValid(d, m, y):
    return True if (m in [1,3,5,7,8,10,12] and 1<=d<=31) or (m in [2,4,6,9,11] and 1<=d<=30) or (m==2 and (isLeapYear(y) and 1<=d<=29) or (not isLeapYear(y) and 1<=d<=28)) else False

#Get the date
y = int(raw_input("Year: "))
while y<0: y = int(raw_input("Year: "))
m = int(raw_input("Month: "))
while m < 0 and m > 12: m = int(raw_input("Month: "))
d = int(raw_input("Day: "))
while not isDayValid(d, m, y): d = int(raw_input("Day: "))

#Select new year
if d==31 and m==12: new_y = y+1
else: new_y = y

#Select new day and month
if (m in [1,3,5,7,8,10,12] and d==31) or (m in [2,4,6,9,11] and d==30) or (m==2 and isLeapYear(y) and d==29) or (m==2 and not isLeapYear(y) and d==28):
    new_d = 1
    if m==12: new_m = 1
    else: new_m = m+1
else:
    new_d = d+1
    new_m = m

#Print everything
print  str(new_d) + "-" + str(new_m) + "-" + str(new_y)


