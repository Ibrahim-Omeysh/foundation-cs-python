############# class tasks #########
class Task:

    def __init__(self, task_id,task_description,task_priority):
        self.__id=task_id
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
    
############################### class node #############################

class Node:
    def __init__(self,info,desc):
        self.__info=info
        self.__next=None
        self.__desc=desc

############################ class queuetask #############################
class queuetask:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0

    def isEmpty(self):
        return self.__size==0
    
    def enqueue(self,info):###### adding new task according to his priority##########
        node_to_add=Node(info)

        if self.__size==0:
            self.__head=node_to_add
            self.__tail=node_to_add
            self.__size+=1
            print("task added successfully")
        else:
            if (node_to_add.__info >self.__head.__info):###### the priority is bigger than the priority of first node ########
                node_to_add.__next=self.__head
                self.__head=node_to_add
                self.__size+=1
                print("task added successfully")
            else:               ########## if not we had to search for it ###############
                current=self.__head
                previous=current
                while current!=None and current.__info>=node_to_add.__info:####### find the node that hade smaller priority ########
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
            return temp.__info
    
    def displayQueue(self):#### displaying tasks #####
        current=self.__head
        while current.__next!=None:
            print("task :" ,current.__desc," with priority:", current.__info,end="\n")
            current=current.__next
        print("task :" ,current.__desc , " with priority:", current.__info ,end="\n")