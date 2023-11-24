# https://stackoverflow.com/questions/1045344/how-do-you-create-an-incremental-id-in-a-python-class
# https://www.geeksforgeeks.org/priority-queue-in-python/
# https://www.studytonight.com/code/python/ds/priority-queue-in-python.php

############# class tasks #########
class Task:
    task_id=0
    def __init__(self, task_description,task_priority):
        Task.task_id+=1
        self.__id=Task.task_id
        self.__description=task_description
        self.__priority=task_priority
        self.__completed=False
    ########### setter and getter for fields #############
    
    ############### id #############################
    def getId(self):
        return self.__id
    ############### description #############################
    def setDescription(self,description):
        self.__description=description
    def getDescription(self):
        return self.__description
     ############### priority #############################
    def setPriority(self,priority):
        self.__priority=priority
    def getPriority(self):
        return self.__priority 
     ############### completed #############################
    def setCompleted(self,completed):
        self.__completed=completed
    def getCompleted(self):
        return self.__completed
    
    def printTask(self):
        print("-id-: ",self.__id,"-description-: ",self.__description,"-priority-: ",self.__priority,"\n")
    
############################### class node #############################

class Node:
    def __init__(self,task:Task):
        self.__task = task
        self.next=None
    def getTask(self):
        return self.__task
    

############################ class queuetask #############################
class Queuetask:
    def __init__(self):
        self.__head=None
        self.__size=0

    def getHead(self):
        return self.__head
    
    def isEmpty(self):
        return self.__size==0
    
    def enqueue(self,task:Task):###### adding new task according to his priority##########
        node_to_add=Node(task)

        if self.__size==0:
            self.__head=node_to_add
            self.__size+=1
            print("\n-----task added successfully------\n")
        else:
            if (node_to_add.getTask().getPriority()> self.__head.getTask().getPriority()):### the priority is bigger than the priority of first node #####
                node_to_add.next=self.__head
                self.__head=node_to_add
                self.__size+=1
                print("\n-----task added successfully------\n")
            else:               ########## if not we had to search for it ###############
                current=self.__head
                previous=current
                while ( current!=None and current.getTask().getPriority() >= node_to_add.getTask().getPriority() ):### find the node that hade smaller priority #####
                    previous=current
                    current=current.next

                ######### adding node between previous and next node ###############
                previous.next=node_to_add
                node_to_add.next=current
                self.__size+=1
                print("\n-----task added successfully------\n")

    def dequeue(self): ##### pop the first element from the queue #####
        if self.isEmpty():
            print("Your queue is empty")
        else:
            temp=self.__head
            self.__head=self.__head.next
            temp.next=None
            self.__size-=1
            return temp.getTask()
    
    def displayQueue(self):#### displaying tasks #####
        current=self.__head
        while (current.next !=None):
            current.getTask().printTask()
            current=current.next
        current.getTask().printTask()
    
############# class stack####################
    
class Stack:
    def __init__(self):###### initail definition###########
        self.__head=None
        self.__size=0
    
    def isEmpty(self):##### return if empty #####
        return self.__size==0
    
    def push(self,task:Task):###### add node to stack #####
        node_to_add=Node(task)
        node_to_add.next=self.__head
        self.__head=node_to_add
        self.__size+=1
        print("task added successfully to stack")

    def pop(self):#### delet node from stack ###########
        temp=self.__head
        self.__head=self.__head.next
        temp.next=None
        self.__size-=1
        print("task removed successfully from stack")

    def displayStack(self):###### printing items in stack ########
        if self.__size==0:
            print("empty stack")
        else:
            current=self.__head
            while current.next != None:
                current.getTask().printTask()
                current=current.next
            current.getTask().printTask()

################## Class Task manager#################
class TaskManager:
    def __init__(self):######## initial definition ###############
        self.__task_queue=Queuetask()
        self.__task_history=Stack()

    ############## set and get functions #############
    def getTaskHistory(self):
        return self.__task_history
    
    def setTaskHistory(self,newTaskHistory):
        self.__task_history=newTaskHistory 

    def setTaskQueue(self,newTaskQueue):
        self.__task_queue=newTaskQueue

    def getTaskQueue(self):
        return self.__task_queue
     
    ############ display functions #################
    def displayTaskHistory(self):
        self.__task_history.displayStack()
       
    def displayTaskQueue(self):
        self.__task_queue.displayQueue()

    ######### class finished #########################

############# function for verify input #############

def verifyDescription():##### function for verify description #########
    description=input("please, insert description:")
    while not description.isalpha():
        description=input("please, insert title without special characters:")
    return description

def verifyPriority():###### function for verify priority ########
    priority=input("please, insert priority between 1 and 100:")
    while not priority.isnumeric() or int(priority)<1 or int(priority)>100:
        priority=input("please, insert priority between 1 and 100:")
    return priority

def verifyId():###### function for verify id ########
    id=input("please, insert id:")
    while not id.isnumeric():
        id=input("please, insert a positive number:")
    return id

########### function search task bi id ################

def searchTaskById(id,q1:Queuetask):
    current=q1.getHead()
    while current!=None:
        if current.getTask().getId()==int(id):
            return current
        else:
            current=current.next
    return current

#################### menu #######################################
def displayMenu():

    q1=Queuetask()
    st1=Stack()
    tm1=TaskManager()
    
    n=0
    while n!=7:
        print("1. Add a new task.")
        print("2. get task by id.")
        print("3. complete high priority task.")
        print("4. display all task.")
        print("5. display uncompleted task.")
        print("6. display last completed task.")
        print("7. exit.")
        print("_______________________________________________________________")
        n=input('\nplease choose an option: ')

        #####----- check on input option ---------########
        while not n.isnumeric() or int(n)<1 or int(n)>7:
            n=input("please insert number between 1 and 7 : ")

        n=int(n)
        if n==1:########## adding new task to task manager ##############
            descrption=verifyDescription()
            priority=verifyPriority()
            task1=Task(descrption,priority)
            q1.enqueue(task1)
            tm1.setTaskQueue(q1)

        if n==2:############# find task by id ################
            id=verifyId()
            task=searchTaskById(id,q1)
            if task==None:
                print("\nid not found please try again")
            else:
                task.getTask().printTask()
        
        if n==3:######### complete high priority task ##############
           st1.push(q1.dequeue()) 
           tm1.setTaskHistory(st1)
           print("\n Marking the highest priority task as completed and putting it in the task history successfully")

            

################## main ###########################

def main():
    displayMenu()
main()
