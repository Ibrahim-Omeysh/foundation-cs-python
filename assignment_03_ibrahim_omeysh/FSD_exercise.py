##### print class #########
def printClass(dect):
    for key,value in dect.items():
        print ('Student Id:',key , ' ---information---:' , value)

##### find key to a specific value  #########
def findKey(dict1,val):
    for key ,value in dict1.items():
        if val==value:
            return key
        if isinstance(value,dict):
            if findKey(value,val):
                return key
        else:
            return None
        
###### find  information #######  
 
def findInformation(dict1,info):
    x=[]
    for key , val in dict1.items():
        x.append(dict1[key].get(info))
    return x        
        
######   calculate average ########

def studentAverage(dict1):
    list1=findInformation(dict1,"scores")
    list2=[]
    for i in range(len(list1)):
        avg=sum(list1[i])/3
        list2.append(avg)
    return list2    


####### youngest student ########

def youngestStudent(dict1):
    list1=findInformation(dict1,"age")
    youngest=list1.index(min(list1))+1
    return dict1[youngest]

###### high score ########

def highScore (dict1):
    list1=studentAverage(dict1)
    highestscore=list1.index(max(list1))+1
    return dict1[highestscore]

######## ADD student #########

###### first insert name ######
def insertName():
    name=input("please insert the name of the student: ")
    while not name.isalpha():
        name=input("please insert a valide name")
    return name

###### second insert age ######
def insertAge():
    validnumber=False
    while not validnumber:
        age=input("please insert the age:")
        if age.isdigit():
            age=int(score)
            if age <=60 and age>16:
                validnumber=True
                return age
            else:
                print("The Age is not between 16 and 60. Please try again.")
        else:
            print('the input is not an age, try again')
     
    

####### third insert scores #######
def insertScores():
    list1=[]
    for i in range(3):
        validnumber=False
        while not validnumber:
            score=input("please insert the score:")
            if score.isdigit():
                score=int(score)
                if score <=100:
                    list1.append(score)
                    validnumber=True
                else:
                    print("The score is not between 0 and 100. Please try again.")
            else:
                print('the input is not a valid score, try again')
    return list1

########## now we add a student ########

def addStudent(dict1):
    name=insertName()
    age=insertAge()
    scores=insertScores()
    dict1[int(len(dict1)+1)]={'name':name,'age':age ,"scores":scores}
    return dict1
############ ^^^^^FINISH ADD STUDENT STEPS^^^^^^#########

######## remove student ########

def removeStudent(dict1):
    name =insertName()
    studentremove=findKey(dict1,name)
    dict1.pop(studentremove)
    return dict1

######## find common names student###############
             

   
    
def main():
    classroom ={1:{"name" : "ibrahim" ,"age":"29",  "scores":(25,75,95)},
                2:{"name" : "georgio" ,"age":"20",  "scores":(65,70,95)},
                3:{"name" : "ali"     ,"age":"25",  "scores":(25,45,65)},
                4:{"name" : "ahmad"   ,"age":"23",  "scores":(30,40,20)},
                5:{"name" : "omar"    ,"age":"24",  "scores":(95,40,90)}
               }
    print(removeStudent(classroom))

    
main()