import sys
import string

filename = ""

def make_rot_n(n):
 lc = string.ascii_lowercase
 uc = string.ascii_uppercase
 trans = string.maketrans(lc + uc,
                          lc[n:] + lc[:n] + uc[n:] + uc[:n])
 return lambda s: string.translate(s, trans)

with open(filename, 'r') as file:
    st = file.read()

abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
variety = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for c in st:
    for i in range(len(abc)):
        if abc[i] == c:
            variety[i] += 1

for i in range(len(abc)):
    print("%c is found: %i time(s)" % (abc[i], variety[i]))

for j in range(len(variety)):
    if variety[j] == max(variety):
        mostCom = abc[j]
        break

print("Most frequent letter: " + mostCom)
    
