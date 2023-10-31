##### print class #########
def printClass(dect):
    for key,value in dect.items():
        print ('Student Id:',key , ' ---information---:' , value)

##### find key  #########
def findKey(dict1,val):
    for key ,value in dict1.items():
        if val==value:
            return key
        if isinstance(value,dict):
            if findKey(value,val):
                return key
        else:
            return None
        
######   calculate average ########
def dectAverage(dict1,k):
    scores=dict1[k]["scores"]
    mean=0
    for i in scores: 
        mean +=int(scores[i] )
    return mean/3    

    
    



def main():
    classroom ={1:{"name" : "ibrahim" ,"age":"29",  "scores":(25,40,95)},
                2:{"name" : "georgio" ,"age":"20",  "scores":(65,70,95)},
                3:{"name" : "ali"     ,"age":"25",  "scores":(25,45,65)},
                4:{"name" : "ahmad"   ,"age":"23",  "scores":(30,40,20)},
                5:{"name" : "ibrahim"    ,"age":"24",  "scores":(95,40,95)}
               }
    print(dectAverage(classroom, findKey(classroom,"ibrahim")))
    
main()