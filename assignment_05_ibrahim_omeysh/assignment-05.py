#https://www.geeksforgeeks.org/python-validate-string-date-format/
#https://www.itsolutionstuff.com/post/how-to-sort-list-by-date-in-pythonexample.html
#https://github.com/AharonSambol/PrettyPrintTree#tree

from datetime import datetime
from PrettyPrint import PrettyPrintTree

####################   class node ###############################
class Node:
    def __init__(self, name, fname, bdate):
        self.name= name
        self.fname= fname
        self.bdate= bdate
        self.children = []
        self.parent = None

    def addChild(self, child):
        self.children.append(child)
        return child

    def __str__(self):
        return f"{self.name} {self.fname} {self.bdate}"


################## class family tree ##########################
class FamilyTree:
    def __init__(self,root:Node):
        self.__root = root

    def getRoot(self):
        return self.__root

    ################ search ####################

    def search(self,searched_person:Node,parent:Node):
        if parent ==None:
            return None

        if (searched_person.name==parent.name and searched_person.fname==parent.fname and searched_person.bdate==parent.bdate):
            return searched_person

        for child in parent.children:
            found_child=self.search(searched_person ,child)
            if found_child is not None:
                return found_child
            else:
                f"not found"

    ################ add child ####################

    def addChild(self, parent_node, child_node:Node):
        parent_node = self.search(parent_node,self.__root)
        if parent_node is not None and child_node not in parent_node.children:
            parent_node.addChild(child_node)
            child_node.parent=parent_node
            print("Child added successfully")
        else:
            print("child already exists")

    ####################### sort birthday ###############################
    def listBirthDate(self ,node:Node, listbirthdate:list):
        if node is not None:
            listbirthdate.append(node.bdate)
            for child in node.children:
                self.listBirthDate(child, listbirthdate)
        return listbirthdate


    def sortBirthdate(self,list1):
        list1=self.listBirthDate(self.getRoot(),list1)
        list1.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
        print(list1)

##### validate date ############
def validDate(date):
    format = "%d-%m-%Y"
    while not datetime.strptime(date, format):
        date = input("Enter a valid date DD-MM-YYYY: ")
    return date
################# finding relation between nodes #############################

##### find the high relation ##############
def relation(parent:Node ,searched_person:Node,family:FamilyTree,level):
        if parent==searched_person:
            return level
        for child in parent.children:
            high=relation(child,searched_person,family,level+1)
            if high>0:
                return  high
        return -1
 ####### print relation #######################
def printRelation(parent:Node ,searched_person:Node,family:FamilyTree):
    rel1=relation(family.getRoot(),parent,family,0)
    rel2=relation(family.getRoot(),searched_person,family,0)

    print(rel1,rel2)
    if parent.parent==searched_person.parent:
        print(f"{searched_person.name} and {parent.name} are brother")
    else:
            if rel1==rel2 and relation(family.getRoot(),searched_person.parent,family,0)==relation(family.getRoot(),parent.parent,family,0):
                print(f"{parent.name} and {searched_person.name} are cousins")
            if (rel2-rel1)==1:
                print(f"{searched_person.name} is a child of {parent.name}")
            if (rel2-rel1)==2:
                print(f"{searched_person.name} is a grandson of {parent.name}")
            if (rel2-rel1)==3:
                print(f"{searched_person.name} is a great-grandson of {parent.name}")
            if (rel2-rel1)>3:
                print(f"{searched_person.name} is a {rel2-rel1}X-grandson of {parent.name}")

################# count name ###########################

def countNames(name,root:Node,counter):
    if root.name==name:
        return counter+1
    for child in root.children:
        countername=countNames(name,child,counter+1)
        if countername>0:
            return countername
    return 0

################# menu #######################
# def menu():
#     print("1. Add child")
#     print("2. Sort by birthday")
#     print("3. Print relation")
#     print("4. Count name")
#     print("5. Exit")
#     print("Enter your choice: ")
#     return int(input())


################################ main #################################

def main():
#     n=0
#     print("first we need to add the first member of the family")
#     name=input("Enter the name: ")
#     fname=input("Enter the family name: ")
#     bdate=validDate(input("Enter the birthday: "))
#     p=Node(name,fname,bdate)
#     family=FamilyTree(p)
#     while n<5:
#         n=menu()
#         if n==1:
#             name=input("Enter the name: ")
#             fname=input("Enter the family name: ")
#             bdate=validDate(input("Enter the birthday: "))
#             p=Node(name,fname,bdate)
#             family.addChild(p)
#         if n==2:
#             list1=[]
#             family.sortBirthdate(list1)
#             print(list1)
    p=Node("John","omeysh","1-10-1980")
    print(p.__str__())
    p1=Node("karim","omeysh","1-5-1988")
    p2=Node("ibrahim","omeysh","1-10-2000")
    p3=Node("ali","omeysh","4-5-1994")
    p4=Node("ahmad","omeysh","6-8-2007")
    p6=Node("omar","omeysh","5-8-2010")
    p7=Node("karim","omeysh","20-8-2011")
    p8=Node("nader","omeysh","20-9-2012")
    p9=Node("fadi","omeysh","5-8-2013")
    p10=Node("ousama","omeysh","11-8-2014")
    p11=Node("husein","omeysh","13-4-2015")

    cina=FamilyTree(p)
    cina.addChild(p,p1)
    cina.addChild(p,p2)
    cina.addChild(p,p3)
    cina.addChild(p3,p4)
    cina.addChild(p1,p6)
    cina.addChild(p2,p7)
    cina.addChild(p7,p8)
    cina.addChild(p8,p9)
    cina.addChild(p9,p10)
    cina.addChild(p9,p11)
    cina.addChild(p9,p11)
    print(cina.search(p4,p3))
    print(cina.search(p9,p8))
    print(cina.search(p2,p9))

    # list1=[]
    # cina.sortBirthdate(list1)
    # printRelation(p,p10,cina)
    # pt = PrettyPrintTree(lambda x: x.children, lambda x: f"{x.name} {x.fname} {x.bdate}")
    # pt(cina.getRoot())
    # print(countNames("karim", cina.getRoot(),0))
main()