class User:
    def __init__(self,username):
        self.username=username
        self.friends=[]

    def addFriend(self,friend):
        if friend not in self.friends:
            self.friends.append(friend)
        else:
            print(f"{self.username} and {friend.username} are already friends")

    def getFriend(self):
        return self.friends


class Platform:

    def __init__(self):
        self.users={}
    
    def addUser(self, username):
        if username in self.users:
            print("User already exist")
        else:
            added_user=User(username)
            self.users[username]=added_user
            print("User added successfully")
            return added_user


    def removeUser(self,username):
        if username in self.users:
            deleted_user=self.users.pop(username)
            for user1 in self.users.values():
                if deleted_user in user1.friends:
                    user1.friends.remove(deleted_user)
            print(f"{deleted_user.username} deleted successfully")
        else:
            print("User does not exist")
        
    def removeRelation(self,username1,username2):
        user1= self.users[username1]
        user2=self.users[username2]
        if user1 in user2.friends and user2 in user1.friends:
            user2.friends.remove(user1)
            user1.friends.remove(user2)
            print(f"{user1.username} and {user2.username} are no more friends")
        else:
            print(f"{user1.username} and {user2.username} are not friends")




        
    def addRelation(self, user1,user2):
        if user1 in user2.friends or user2 in user1.friends :
            print(f"{user1.username} and {user2.username} are friends already")
        else:
            user2.addFriend(user1)
            user1.addFriend(user2)
            print(f"{user1.username} and {user2.username} are frinds now")

    def printFriend(self):
        for user in self.users:
            for friend in self.users[user].friends:
                print(f"{self.users[user].username} and {self.users[friend].username} are friends")




def main():
    p=Platform()
    u1=p.addUser("omar")
    u2=p.addUser("ali")
    u3=p.addUser("bob")
    u4=p.addUser("md")
    p.addUser("ali")
    p.addRelation(u1,u2)
    p.addRelation(u2,u3)
    p.addRelation(u4,u3)
    p.addRelation(u2,u1)
    #p.removeUser("omar")  
    for i in u2.getFriend():
        print(i.username)
    p.removeRelation("omar","ali")  
    for i in u2.getFriend():
        print(i.username)    

main()