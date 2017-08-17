

class User (object):
    # Define the fields and methods for your object here.
    def __init__(self, username, name, password, bio, userID):
        self.username = username
        self.name = name
        self.password = password
        self.bio = bio
        self.userID = userID
        self.connections = []

    def getUsername(self):
        return self.username
    def getName(self):
        return self.name
    def getBio(self):
        return self.bio
    def getPassword(self):
        return self.password
    def addConnection(self, user2):
        self.connections.append(user2)
    def getUserID(self):
        return self.userID




class Network: #(uncomment later when needed)
    # Define the fields and methods for your object here. Connections go here
    def __init__ (self):
        self.users = []
    #def deleteUser(self,username):
    def numUser(self, user):
        return len(self.users)
    def printUsers(self):
        for users in self.users:
            return users.getUsername()
    def getUserID(self, username):
        userID = -1
        for user in self.users:
            if username == user.getUsername():
                userID = user.getUserID()
        return userID
        #for i in range(0, len(self.users)):
            #if (self.users [i] == username):
                #return i

    def addConnection(self, User1, User2):

    #def printConnections(self, username):
        #for connections in self.users:
            #return users.printconnections()
    #def printUserProfile(self,user):
        #return len(self.users)
    def addUser(self, username, name, password, bio):
        for i in range (0, len(self.users)):
            if (self.users [i] == username):
                print ("Username already taken")
                return
        userID = len(self.users)
        self.users.append(User(username, name, password, bio,userID))



def main():
    # Define the program flow for your user interface here. User input here
# Runs your program.
    myNetwork = Network()
    print("Hello and welcome!")
    username = input ("Please enter a username:")
    name = input ("Please enter your name:")
    password = input ("Please enter a password:")
    bio = input ("Please enter a bio:")

    print("username", username)
    print("name", name)
    print("password", password)
    print ("bio", bio)


    myNetwork.addUser(username, name, password, bio)
    print(myNetwork.printUsers())


    myNetwork.getUserID (username)
    userID=-1
    print(myNetwork.getUserID(username))

    #myNetwork.printConnections (username, connections)
    #print(myNetwork.printConnections())

    #myNetwork.getUserID (username)
    #print (myNetwork.getUserID(Kenzie.getUsername()))


    #Kenzie = User("kenzielovesdogs", "Kenzie", "build1ng", "Hi. I run and like to travel")
    #print(Kenzie.getUsername(), Kenzie.getName(), Kenzie.getPassword(), Kenzie.getBio())

if __name__ == '__main__':
    main()
