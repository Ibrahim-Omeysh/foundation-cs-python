#https://www.geeksforgeeks.org/python-validate-string-date-format/

from datetime import datetime
    
####################   class node ###############################
class Node:
    def __init__(self, name, fname, bdate):
        self.name= name
        self.fname= fname
        self.bdate= bdate
        self.children = []
    
    def addChild(self, child):
        self.children.append(child)

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
            return parent
        
        for child in parent.children:
            found_child=self.search(searched_person ,child)
            if found_child is not None:
                return found_child

    ################ add child ####################
        
    def addChild(self, parent_node, child_node):
        parent_node = self.search(parent_node,self.__root)
        if parent_node is not None:
            parent_node.addChild(child_node)
            print("Child added successfully")
        else:
            print("Parent node not found")


def validDate(date):
    format = "%d-%m-%Y"
    while not datetime.strptime(date, format):
        date = input("Enter a valid date DD-MM-YYYY: ")
    return date

def main():
    p=Node("John","cina","1-10-1980")
    p1=Node("karim","smith","1-5-1988")
    p2=Node("Mary","cina","1-10-1980")
    p3=Node("bob","omeysh","4-5-1994")

    cina=FamilyTree(p)
    cina.addChild(p,p1)
    cina.addChild(p,p2)
    cina.addChild(p2,p3)
    print(cina.search(p3,p1).__str__())
main()