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
    