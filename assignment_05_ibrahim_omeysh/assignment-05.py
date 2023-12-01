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

    ################ add child ####################
        
    def addChild(self, parent_node, child_node:Node):
        parent_node = self.search(parent_node,self.__root)
        if parent_node is not None:
            parent_node.addChild(child_node)
            child_node.parent=parent_node
            print("Child added successfully")
        else:
            print("Parent node not found")

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

##### find the high pf relation ##############
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
                print(f"{searched_person.name} is a great-great-grandson of {parent.name}")

################# count name ###########################     

def countNames(name,family:FamilyTree):
    root=family.getRoot()
    

################################ main #################################

def main():
    p=Node("John","cina","1-10-1980")
    p1=Node("karim","smith","1-5-1988")
    p2=Node("Mary","cina","1-10-2003")
    p3=Node("bob","omeysh","4-5-1994")
    p4=Node("omar","omeysh","6-8-2007")
    p5=Node("abed","omeysh","20-8-2005")
    cina=FamilyTree(p)
    cina.addChild(p,p1)
    cina.addChild(p,p2)
    cina.addChild(p,p3)
    cina.addChild(p3,p4)
    cina.addChild(p1,p5)
    print(cina.search(p3,p4).__str__())
    list1=[]
    cina.sortBirthdate(list1)
    printRelation(p,p5,cina)
    pt = PrettyPrintTree(lambda x: x.children, lambda x: f"{x.name} {x.fname} {x.bdate}")
    pt(cina.getRoot())

main()