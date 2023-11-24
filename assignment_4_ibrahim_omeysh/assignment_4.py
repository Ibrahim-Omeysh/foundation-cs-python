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
                node_to_add.next=self.__head
                self.__head=node_to_add
                self.__size+=1
                print("task added successfully")
            else:               ########## if not we had to search for it ###############
                current=self.__head
                previous=current
                while ( current!=None and current.getTask().getPriority() >= node_to_add.getTask().getPriority() ):####### find the node that hade smaller priority ########
                    previous=current
                    current=current.next

                ######### adding node between previous and next node ###############
                previous.next=node_to_add
                node_to_add.next=current
                self.__size+=1
                print("task added successfully")

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
    def __init__(self):######## initial definitio ###############
        self.__task_queue=Queuetask()
        self.__task_history=Stack()

    def getTaskHistory(self):
        return self.__task_history
    
    def setTaskHistory(self,newTaskHistory):
        self.__task_history=newTaskHistory 

    def setTaskQueue(self,newTaskQueue):
        self.__task_queue=newTaskQueue

    def getTaskQueue(self):
        return self.__task_queue
     

    def displayTaskHistory(self):
        self.__task_history.displayStack()
       
    def displayTaskQueue(self):
        self.__task_queue.displayQueue()



################## main ###########################

def main():
    task1=Task("eating",3)
    task2=Task("gaming",7)
    task3=Task("dressing",9)
    task4=Task("cleaning",1)
    task1.printTask()
    task2.printTask()
    task3.printTask()
    task4.printTask()
    print("____________________starting queue_______________________________")
    tm1=TaskManager()
    q1=Queuetask()
    q1.enqueue(task1)
    q1.enqueue(task2)
    q1.enqueue(task3)
    q1.enqueue(task4)
    tm1.setTaskQueue(q1)
    tm1.displayTaskQueue()
    print("____________________finich queue_______________________________")
    
    print("______________________starting stack_____________________________")
    st=Stack()
    q2=q1.dequeue()
    st.push(q2)
    tm1.setTaskHistory(st)
    tm1.displayTaskHistory()
    
    # print("________________________pop 1 item___________________________")
    # st.pop()
    # st.displayStack()
    # print("________________________pop 2 item___________________________")
    # st.pop()
    # st.displayStack()
main()
