
users = []
currentUser = object

def checkForClonedUsers(nm, usrs):
    for user in usrs:
        if nm == user.name:
            return True
    return False

def createUser():
    name = input("Enter username: ")
    pw = input("Enter password: ")
    while checkForClonedUsers(name,users):
        print("There is already one user with that name, please enter another name and password: ")
        name = input("Enter username: ")
        pw = input("Enter password: ")
    newUser = user(name,pw,0)
    users.append(newUser)

def login():
    name = input("Enter username: ")
    pw = input("Enter password: ")
    for user in users:
        if name == user.name and pw == user._pw:
            currentUser = user
            print("User %s loged" % currentUser.name)
            return 0
    print("Username or password incorrect")

def displayUsers(usrs):
    i = 0
    for user in usrs:
        i += 1
        print("User %i: %s" % (i,user.name))
        
class user(object):
    def __init__(self,name,pw,money): 
        self.name = name
        self._pw = pw
        self._money = money
        
    def accessMoney(self,pw):
        if pw == self._pw:
            return self._money

class admin(user):
    pass
        

#   MAIN LOOP

loop = True

admin = admin("Administrator","lana2016",1000000)
users.append(admin)
unrr = user("Unregistered","none",0)
currentUser = unrr

def exitUser(cu):
    if cu != unrr:
        cu = unrr
        print("Exit succesul")
    else:
        print("Login first to exit")

while loop:

    print("Current user: " + currentUser.name)
    order = input("Command: ") 

    #Comandos
    if order == "display":
        displayUsers(users)
    elif order == "new":
        createUser()
    elif order == "login":
        name = input("Enter username: ")
        pw = input("Enter password: ")
        for user in users:
            if name == user.name and pw == user._pw:
                currentUser = user
                print("User %s loged" % currentUser.name)
                break
        print("Username or password incorrect")
    elif order == "exit":
        exitUser(currentUser)
    else:
        print("Unknow command, try 'help'")


        
    
