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
    def setId(self,id):
        self.__id=id
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
        print(self.__id,self.__description,self.__priority)
    
############################### class node #############################

class Node:
    def __init__(self,task:Task):
        self.__task = task
        self.__next=None
    def getTask(self):
        return self.__task
    

############################ class queuetask #############################
class queuetask:
    def __init__(self):
        self.__head=None
        self.__size=0

    def isEmpty(self):
        return self.__size==0
    
    def enqueue(self,task:Task):###### adding new task according to his priority##########
        node_to_add=Node(task)

        if self.__size==0:
            self.__head=node_to_add
            self.__size+=1
            print("task added successfully")
        else:
            if (node_to_add.getTask().getPriority()> self.__head.getTask().getPriority()):###### the priority is bigger than the priority of first node ########
                node_to_add.__next=self.__head
                self.__head=node_to_add
                self.__size+=1
                print("task added successfully")
            else:               ########## if not we had to search for it ###############
                current=self.__head
                previous=current
                while ( current!=None and current.getTask().getPriority() >= node_to_add.getTask().getPriority() ):####### find the node that hade smaller priority ########
                    previous=current
                    current=current.__next

                ######### adding node between previous and next node ###############
                previous.__next=node_to_add
                node_to_add.__next=current
                self.__size+=1
                print("task added successfully")

    def dequeue(self): ##### pop the first element from the queue #####
        if self.isEmpty():
            print("Your queue is empty")
        else:
            temp=self.__head
            self.__head=self.__head.__next
            temp.__next=None
            self.__size-=1
            print("removed task successfully")
            return temp.__task
    
    def displayQueue(self):#### displaying tasks #####
        current=self.__head
        while (current.__next !=None):
            print(current.getTask().printTask(),end="\n")
            current=current.__next
        print(current.getTask().printTask() ,end="\n")
    
############# class stack####################
    
# class Stack:
#     def __init__(self):
#         self.__head=None
#         self.__size=0


def main():
    task1=Task("eating",3)
    task2=Task("cleaning",7)
    task3=Task("cleaning",9)
    task4=Task("cleaning",1)
    task1.printTask()
    task2.printTask()
    task3.printTask()
    task4.printTask()
    q1=queuetask()
    q1.enqueue(task1)
    q1.enqueue(task2)
    q1.enqueue(task3)
    q1.enqueue(task4)
    q1.displayQueue()
main()
