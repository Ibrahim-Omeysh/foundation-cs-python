class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:

    def __init__(self):
        self.head=None

    def addFreind(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return 
        else:
            new_node.next=self.head
            self.head=new_node

    def searchExisting(self,name):
        current=self.head
        while current !=None:
            if current.data==name:
                return True
            else:
                current=current.next
                return False
        

    # def insertAtIndex(self,data,index):
    #     new_node=Node(data)
    #     pos=0
    #     if pos== index:
    #         self.insertAtFirst(data)
    #     else:
    #         current=self.head
    #         while (current is not None and pos +1 != index):
    #             current=current.next
    #             pos=+1
    #         if current is not None:
    #            new_node.next=current.next
    #            current.next=new_node
    #         else:
    #             print("index is out of range")
    
    # def insertFreind(self, data):
    #     new_node = Node(data)
    #     if self.head is None:
    #         self.head = new_node
    #         return
 
    #     current_node = self.head
    #     while(current_node.next):
    #         current_node = current_node.next
 
    #     current_node.next = new_node

    def removeFriend(self,name):
        if self.head == None:
            print("no freind found")
        if self.head and self.head.data==name:
            self.head=self.head.next
        else:
            current=self.head
            prev=None
            while current :
                if current.data!=name and current:
                    prev=current
                    current=current.next

                if current:
                    prev.next=current.next
                else: 
                    print(f"{name} not found in freinds")

    def printConnected(self):
        current = self.head
        while current is not None:
            print(current.data,end=" --> ")
            current = current.next
        if self.head is None:
            print("No friends connected.")



class User:
    def __init__(self,name):
        self.name=name
        self.connection=Linkedlist()


class Graph:
    def __init__(self):
        self.platform=[]
        self.people={}
        self.index=0

    def addNewPeople(self,name):
        new_people=User(name)
        if new_people in self.platform:
            print("user already exist")
        else:
            self.platform.append(new_people)
            self.people[new_people.name]=self.index
            self.index+=1




    def addConnections(self,name1,name2):
        s1=self.people.get(name1)
        s2=self.people.get(name2)
        if s1 is not None and s2 is not None:
            if self.platform[s1].connection.searchExisting(name2):
                print("Connection already established")
            else:
                self.platform[s1].connection.addFreind(name2)
                self.platform[s2].connection.addFreind(name1)

    def printConnections(self):
        for user in self.platform:
            print(f"{user.name} is connected to:")
            user.connection.printConnected()
            print("\n")



def main():
    platform=Graph()
    platform.addNewPeople("ali")
    platform.addNewPeople("bob")
    platform.addNewPeople("mona")
    platform.addNewPeople("ahmad")
    platform.addConnections("ali","bob")
    platform.addConnections("mona","bob")
    platform.addConnections("ahmad","bob")
    platform.addConnections("ahmad","bob")

    platform.printConnections()
main()