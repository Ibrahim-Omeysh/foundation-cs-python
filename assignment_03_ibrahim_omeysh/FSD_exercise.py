##### print class #########
def printClass(dect):
    for key,value in dect.items():
        print ('\nStudent Id:',key , ' ---information---:' , value)

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
    youngestage=list1[0]
    indexyoungestage=0
    for i in range(1,len(list1)):
        if int(list1[i])<int(youngestage):
            youngestage=list1[i]
            indexyoungestage=i
    return dict1[indexyoungestage+1]   

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
        name=input("please insert a valide name: ")
    return name

###### second insert age ######
def insertAge():
    validnumber=False
    while not validnumber:
        age=input("please insert the age:")
        if age.isdigit():
            age=int(age)
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
    while studentremove is None:
        print("name not found")
        name =insertName()
        studentremove=findKey(dict1,name)
    dict1.pop(studentremove)
    return dict1

######## find common names student###############

def findComonNames(dict1,name):
    list1=findInformation(dict1,"name")
    list2=[]
    for i in range (len(list1)):
        if list1[i]==name:
            list2.append(i+1)
    return list2

######## student improvment ##############

def studentImprovment(dict1):
    list1=findInformation(dict1,"scores")
    list2=[]
    for i in range(len(list1)):
        list3=sorted(list1[i])
        counter=0
        for j in range(3):
            if  list3[j]==list1[i][j]:
                counter+=1
        if counter==3:
            list2.append(i+1)       
    return list2        
        

    
def main():
    classroom ={1:{"name" : "ibrahim" ,"age":"21",  "scores":(25,75,95)},
                2:{"name" : "georgio" ,"age":"40",  "scores":(65,70,95)},
                3:{"name" : "ali"     ,"age":"25",  "scores":(25,45,65)},
                4:{"name" : "ibrahim" ,"age":"19",  "scores":(30,40,20)},
                5:{"name" : "omar"    ,"age":"20",  "scores":(80,85,90)}
               }
    n=0      
    while n != 8:
        print('\n1) Get Average Score \n2) Get Youngest student\n3) Get High Score\n4) Add Student\n5) Remove Student\n6) Get Common Students\n7) Find Students with Consistent Improvement\n8) Exit')
        n=input('\nplease choose an option: ')
        while (not n.isnumeric()):
            n=input('\nplease insert a valid input: ')
        n=int(n)
        ########## Show average ##############
        if n==1:
            list1=studentAverage(classroom)
            for i in classroom:
                print('\n',classroom[i]["name"],'has a scores average = ',list1[i-1])

        ######### shouw youngest ###########
        if n==2 :
            dict2=youngestStudent(classroom)
            print("\n",dict2["name"],'is youngest student with',dict2["age"],'years old')

        ############ show hihg score ###########
        if n==3:
            dict3=highScore(classroom)
            print('\n', dict3["name"],'has the highest scores =',dict3["scores"])

        ########## add student ########
        if n==4:
            classroom=addStudent(classroom)
            printClass(classroom)
        ######## remove student #########
        if n==5:
            removeStudent(classroom)    
            printClass(classroom)

        ##### Get Common Students #########
        if n==6:
            comonname=insertName()
            listofindex=findComonNames(classroom,comonname)
            if listofindex is None:
                print("sorry ,this name: ",comonname, 'is not in class')
            elif len(listofindex)==1:
                print('sorry we only had 1 student name ',comonname)
            else:
                print('we found',len(listofindex),'students where there name:',comonname)
                for i in range(len(listofindex)):
                    print(classroom[(listofindex[i])])

        ########### Find Students with Consistent Improvement################### 
        if n==7:
            list7=studentImprovment(classroom)
            if list7 is None:
                print("no one in class has a remarkable improvment")
            else:
                print('we found',len(list7),'student')
                for i in range(len(list7)):
                    print(classroom[(list7[i])])
                    





    
main()